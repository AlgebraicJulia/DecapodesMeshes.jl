# Note:
# This script was not used to create unit_icosphere.obj..
# That mesh was made manually in Blender.
# This script is an attempt to make that mesh but has not been run yet!

import bmesh
import bpy
import mathutils
import os

# Get a handle to a new BMesh.
bm = bmesh.new()

#bpy.ops.mesh.primitive_ico_sphere_add(location=(0.0,0.0,0.0), size=1.0)
# (bmesh, subdividsions, diameter, matrix, calculate default UVs)
bmesh.ops.create_icosphere(bm, 4, 2.0, Matrix.Identity(3), false)

me = bpy.data.meshes.new("UnitIcosphereMesh")
bm.to_mesh(me)
bm.free()

unit_icosphere = bpy.data.objects.new("UnitIcosphere", me)
bpy.context.collection.objects.link(unit_icosphere)

blend_file_path = bpy.data.filepath
directory = os.path.dirname(blend_file_path)
target_file = os.path.join(directory, "unit_icosphere.obj")

bpy.ops.export_scene.obj(filepath=target_file, check_existing=True,
  axis_forward='-Z', axis_up='Y', filter_glob="*.obj;*.mtl",
  use_selection=False, use_animation=False, use_mesh_modifiers=True,
  use_edges=True, use_smooth_groups=False, use_smooth_groups_bitflags=False,
  use_normals=False, use_uvs=False, use_materials=True, use_triangles=False,
  use_nurbs=False, use_vertex_groups=False, use_blen_objects=True,
  group_by_object=False, group_by_material=False, keep_vertex_order=False,
  global_scale=1, path_mode='AUTO')
