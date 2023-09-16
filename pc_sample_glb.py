import os
import open3d as o3d
import numpy as np

def sample_point_cloud_from_glb(glb_file, num_samples=15000):
    if os.path.isfile(glb_file):
        print(f"The file at path {glb_file} exists.")
    else:
        print(f"The file at path {glb_file} does not exist.")

    # 1: Read the glb file
    mesh = o3d.io.read_triangle_mesh(glb_file)
    print("The mesh is ", mesh)

    # 2. Sample the points from meshes uniformly
    point_cloud = mesh.sample_points_uniformly(num_samples)

    # 3. Create the Open3D point cloud object
    #point_cloud = o3d.geometry.PointCloud()
    #point_cloud.points = o3d.utility.Vector3dVector(np.asarray(points.points))
    points = np.asarray(point_cloud.points)

    # 4. Save the point cloud to npy files
    file_name = glb_path.split("/")[-1].split(".")[0]
    print(file_name)
    output_path = "./" + file_name + ".npy"
    # o3d.io.write_point_cloud(output_path, point_cloud)
    np.save(output_path, points)

 # 0b823253-c998-50f9-990b-d1bab192ba78.glb
 # 80ffa83f-9903-5983-a99a-b71506261251.glb
 # 95ea28bf-ee6c-5158-858b-49f9e6529bec.glb
 # 7f378cb8-759f-5a4d-9d54-10c306d212b4.glb
 # 0fc021b6-fc83-5cde-bfe4-75175ef2eea8.glb
# glb_path = r"/home/yipeng/objaverse-xl/objaverse-tests/smithsonian/objects/0fc021b6-fc83-5cde-bfe4-75175ef2eea8.glb"
# thing-2609614-file-4257308.stl

glb_path = '/home/yipeng/objaverse-xl/objaverse-tests/thingiverse/thing-2609614-file-4257308.stl'

sample_point_cloud_from_glb(glb_path)


