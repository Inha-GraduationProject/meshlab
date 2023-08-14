import pymeshlab
from pymeshlab.pmeshlab import Percentage

ms = pymeshlab.MeshSet()

ms.load_new_mesh('../source/test.ply')
ms.apply_filter('compute_normal_for_point_clouds')
ms.apply_filter('generate_surface_reconstruction_screened_poisson')
# mesh = ms.apply_filter('compute_texcoord_parametrization_triangle_trivial_per_wedge', 0, 4096, 0, 0)
ms.compute_texcoord_parametrization_triangle_trivial_per_wedge(sidedim=0, textdim=1024, border=0, method=0)
# ms.apply_filter('transfer_attributes_to_texture_per_vertex', 0, 0, 0, 2, 'texture.png', 4096, 4096)
# ms.transfer_attributes_to_texture_per_vertex(sourcemesh=0, targetmesh=0, attributeenum=0, upperbound=2, textname='texture.png', textw=4096, texth=4096)
ms.transfer_vertex_attributes_to_texture_1_or_2_meshes(sourcemesh=0, targetmesh=1, attributeenum=0, upperbound=2.0, textname='texture.png', textw=4096, texth=4096, overwrite=False, assign=False, pullpush=True)
# ms.transfer_attributes_to_texture_per_vertex(0, 0, 0, 2, 'texture.png', 4096, 4096, False, True)
# ms.transfer_vertex_attributes_to_texture_1_or_2_meshes(sourcemesh=0, targetmesh=0, cou)


ms.save_current_mesh('test.obj', True, True, True, True, True, True, True)