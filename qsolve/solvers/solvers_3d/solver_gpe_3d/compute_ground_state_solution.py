from qsolve.core import qsolve_core


def compute_ground_state_solution(self, kwargs):

    tau_0 = kwargs["tau_0"] / self.units.unit_time

    n_iter = kwargs["n_iter"]

    N = kwargs["N"]

    self.psi_0 = qsolve_core.compute_ground_state_solution_gpe_3d(
        self.V,
        self.dx,
        self.dy,
        self.dz,
        tau_0,
        n_iter,
        N,
        self.hbar,
        self.m_atom,
        self.g)
