# import pygltflib
from pygltflib import GLTF2 #, GLTF2Loader


glb_path = "./objaverse-tests/smithsonian/objects/0b823253-c998-50f9-990b-d1bab192ba78.glb"
# red .glb file
with open(glb_path, 'rb') as f:
    data = f.read()

# TO parse the glb file
# gltf = GLTF2Loader(data)
gltf = GLTF2(data)
# print(gltf)"""
"""
The content of the gltf file:

# GLTF2(extensions=b'glTF\x02\x00\x00\x00\xa8\xa7\x0c\x00 \x05\x00\x00
# JSON{"accessors":[{"componentType":5126,"count":89400,"max":[53.9103012084961,44.0028305053711,-1.99890899658203],
# "min":[3.7404351234436,17.539400100708,-32.9975509643555],"type":"VEC3"},{"componentType":5126,"count":89400,"type":"VEC3"}
# ,{"componentType":5126,"count":89400,"type":"VEC2"},{"componentType":5125,"count":450000,"type":"SCALAR"}],
# "asset":{"generator":"MeshSmith mesh conversion tool","version":"2.0"},"bufferViews":[{"buffer":0,"byteLength":417644},
# {"buffer":0,"byteLength":113569,"byteOffset":417644},{"buffer":0,"byteLength":296798,"byteOffset":531213}],
# "buffers":[{"byteLength":828011}],"extensionsRequired":["KHR_draco_mesh_compression"],"extensionsUsed":["KHR_draco_mesh_compression"],
# "images":[{"bufferView":1,"mimeType":"image/jpeg"},{"bufferView":2,"mimeType":"image/jpeg"}],
# "materials":[{"name":"default","normalTexture":{"index":1},"occlusionTexture":{"index":0},
# "pbrMetallicRoughness":{"metallicFactor":0.100000001490116,"roughnessFactor":0.800000011920929}}],
# "meshes":[{"primitives":[{"attributes":{"NORMAL":1,"POSITION":0,"TEXCOORD_0":2},
# "extensions":{"KHR_draco_mesh_compression":{"attributes":{"NORMAL":1,"POSITION":0,"TEXCOORD_0":2},"bufferView":0}},
# "indices":3,"material":0,"mode":4}]}],"nodes":[{"mesh":0}],"scene":0,"scenes":[{"nodes":[0]}],"textures":[{"source":0},{"source":1}]}
"""

# check scenes
print(f"Number of scenes in the glb file: {len(gltf.scenes)}")

# check the number of nodes
for scene_idx, scene in enumerate(gltf.scenes):
    print(f"Scene {scene_idx + 1}:")
    print(f"Number of nodes in scene: {len(scene.nodes)}")

# check materials and textures
print("Materials:")
for material_idx, material in enumerate(gltf.materials):
    print(f"Material {material_idx + 1}: {material.name}")

print("Textures:")
for texture_idx, texture in enumerate(gltf.textures):
    print(f"Texture {texture_idx + 1}: {texture.name}")