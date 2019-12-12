class Planet:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.v_x = 0
        self.v_y = 0
        self.v_z = 0
        self.gravity_x = 0
        self.gravity_y = 0
        self.gravity_z = 0

    @property
    def energy_pot(self):
        return abs(self.x) + abs(self.y) + abs(self.z)

    @property
    def energy_kin(self):
        return abs(self.v_x) + abs(self.v_y) + abs(self.v_z)

    @property
    def total_energy(self):
        return self.energy_kin * self.energy_pot
