from glcontext import *

gl = GLContext()

gl.set_clear_color(1.0, 1.0, 1.0, 1.0)

gl.set_uniform("matrix",
               np.array([
                   [2.0, 0.0, 0.0],
                   [1.0, 2.0, 3.0],
                   [1.0, 0.0, 2.0],
               ]))

gl.set_attributes("position", np.array([
    [1.0, 1.0],
    [1.0, 0.0],
    [0.0, 1.0],
]))

gl.set_attributes(
    "color",
    np.array([
        [0.0, 0.0, 1.0, 0.0],
        [0.0, 1.0, 0.0, 0.0],
        [1.0, 0.0, 1.0, 0.0],
    ]))

gl.set_count(3)


# dumy vertex shader
def vertex_shader(attribute: dict, uniform: dict) -> np.ndarray:
    matrix = uniform["matrix"]
    vertex = attribute["position"]
    for _ in range(3 - vertex.shape[0]):
        vertex = np.append(vertex, 0.0)
    vertex = np.append(np.matmul(matrix, vertex), 0.0)
    return vertex


gl.vShader = vertex_shader
gl.assembly_scheme = Point