import pymeshlab
from pymeshlab.pmeshlab import Percentage

ms = pymeshlab.MeshSet()

ms.load_new_mesh('../source/test.ply')
ms.compute_normal_for_point_clouds()
# ms.apply_filter('compute_normal_for_point_clouds')
ms.generate_surface_reconstruction_screened_poisson()
# ms.apply_filter('generate_surface_reconstruction_screened_poisson')
ms.compute_texcoord_parametrization_triangle_trivial_per_wedge(sidedim=, textdim=4096, border=0, method=0)
# mesh = ms.apply_filter('compute_texcoord_parametrization_triangle_trivial_per_wedge', 0, 4096, 0, 0)
ms.invert_faces_orientation(forceflip=True, onlyselected=False)
ms.save_current_mesh('target.obj')0

ms.transfer_vertex_attributes_to_texture_1_or_2_meshes(sourcemesh=0, targetmesh=1, attributeenum=0, upperbound=pymeshlab.pmeshlab.Percentage(2.0), textname='../meshLab/texture.png', textw=4096, texth=4096, overwrite=False, pullpush=True)
ms.save_current_mesh('output.obj')