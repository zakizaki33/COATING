# https://www.youtube.com/watch?v=AmP_ipy2PhI
# https://courses.ansys.com/index.php/courses/getting-started-with-pymapdl/lessons/overview-of-pymapdl-lesson-1/

from ansys.mapdl.core import launch_mapdl
# mapdl = launch_mapdl()
# print(mapdl)

# https://hpcmemo.hatenablog.com/entry/2021/12/29/012419

import pyvista as pv
from pyvista import examples
# download an example and display it using physically based rendering.
mesh = examples.download_lucy()
mesh.plot(color='lightgrey', pbr=True, metallic=0.2,
          jupyter_backend='pythreejs')

print(pv.__version__)
