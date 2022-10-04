using FileIO
using GeometryBasics
using MeshIO

include("../src/spherical_meshes.jl")

import MeshIO: save

function save(fn::File{format}, msh::T) where {format, T<:EmbeddedDeltaSet2D}
  converted_msh = GeometryBasics.Mesh(msh)
  save(fn, converted_msh)
end

unit_tie_gcm, npi, spi = makeSphere(0, 180, 5, 0, 360, 5, 1)

const EARTH_RADIUS = 6371 #km
const THERMOSPHERE_ALTITUDE = 90 #km
thermo_tie_gcm, npi, spi = makeSphere(0, 180, 5, 0, 360, 5,
  EARTH_RADIUS+THERMOSPHERE_ALTITUDE)

@assert nparts(unit_tie_gcm, :V)   == nparts(thermo_tie_gcm, :V)
@assert nparts(unit_tie_gcm, :E)   == nparts(thermo_tie_gcm, :E)
@assert nparts(unit_tie_gcm, :Tri) == nparts(thermo_tie_gcm, :Tri)

save(File{format"OBJ"}("meshes/unit_tie_gcm.obj"), unit_tie_gcm)
save(File{format"OBJ"}("meshes/thermo_tie_gcm.obj"), thermo_tie_gcm)

