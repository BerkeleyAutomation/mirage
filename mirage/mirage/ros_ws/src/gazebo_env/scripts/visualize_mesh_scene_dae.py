import trimesh
import open3d as o3d
import numpy as np
# Load the 3D scene from the DAE file using trimesh
dae_file_path = "/home/benchturtle/cross_embodiment_ws/src/gazebo_env/meshes/panda/visual/link6.dae"
scene = trimesh.load(dae_file_path)

# Extract the geometry (triangular meshes) from the loaded scene
meshes = scene.geometry
for mesh in meshes:
    if(mesh != 'Shell006_000-mesh'):
        vertices = o3d.utility.Vector3dVector(meshes[mesh].vertices)
        triangles = o3d.utility.Vector3iVector(meshes[mesh].faces)
        open3d_mesh = o3d.geometry.TriangleMesh(vertices, triangles)
        open3d_mesh.translate(np.array([0,0,-0.011791708069958752]))
        meshes[mesh] = trimesh.Trimesh(vertices=open3d_mesh.vertices,faces=open3d_mesh.triangles)
#meshes['Shell012_000-mesh'] = trimesh.Trimesh(vertices=open3d_mesh.vertices,faces=open3d_mesh.triangles)
mesh = trimesh.util.concatenate(tuple(trimesh.Trimesh(vertices=g.vertices, faces=g.faces)
                                   for g in meshes.values()))
#vertices = o3d.utility.Vector3dVector(mesh.vertices)
#triangles = o3d.utility.Vector3iVector(mesh.faces)
#open3d_mesh = o3d.geometry.TriangleMesh(vertices, triangles)
# import pdb
# pdb.set_trace()
vertices = o3d.utility.Vector3dVector(mesh.vertices)
triangles = o3d.utility.Vector3iVector(mesh.faces)
open3d_mesh = o3d.geometry.TriangleMesh(vertices, triangles)
# open3d_mesh.translate(np.array([0,0,-0.011791708069958752]))
pcd = open3d_mesh.sample_points_uniformly(number_of_points=200000)
mesh_coordinate_frame = o3d.geometry.TriangleMesh.create_coordinate_frame(size=0.1,origin=[0,0,0])
# # Visualize the scene using Open3D
# print(np.min(pcd_data[:, 2]) - np.min(pcd2_data[:, 2]))
# print(np.max(pcd2_data[:, 2]) - np.min(pcd2_data[:, 2]))

o3d.visualization.draw_geometries([pcd,mesh_coordinate_frame])
# 'Shell012_000-mesh'
#   ('Shell006_000-mesh', <trimesh.Trimesh(vertices.shape=(1575, 3), faces.shape=(746, 3))>)])