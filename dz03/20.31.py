
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# ============================================================
#                   DrunkardND — n-вимірна модель
# ============================================================
class DrunkardND:
    """
    Модель випадкової ходи у n-вимірному просторі.
    """

    def __init__(self, num_drunkards, dim, init_pos=None,
                 is_limited=False, bounds=None):
        self.num = num_drunkards
        self.dim = dim
        self.is_limited = is_limited
        self.bounds = bounds

        # Початкові позиції
        if init_pos is None:
            self.pos = np.zeros((dim, num_drunkards))
        else:
            self.pos = np.array(init_pos, dtype=float)

        # Якщо область обмежена — ставимо всіх у центр
        if self.is_limited and bounds is not None:
            mins = np.array(bounds[0], dtype=float)
            maxs = np.array(bounds[1], dtype=float)

            # ------------------- FIX -------------------
            # Автоматичне розширення bounds до dim
            if len(mins) != dim:
                mins = np.tile(mins[0], dim)
            if len(maxs) != dim:
                maxs = np.tile(maxs[0], dim)
            # -------------------------------------------

            center = (mins + maxs) / 2
            self.pos = np.tile(center.reshape(dim, 1), (1, num_drunkards))

        # Створення можливих рухів: +1, -1 по кожній осі
        dirs = []
        for i in range(dim):
            d = np.zeros(dim)
            d[i] = 1
            dirs.append(d.copy())
            d[i] = -1
            dirs.append(d.copy())
        self.dirs = np.array(dirs).T  # транспоновано

    # --------------------------------------------------------
    def _push_into_bounds(self):
        mins = np.array(self.bounds[0]).reshape(self.dim, 1)
        maxs = np.array(self.bounds[1]).reshape(self.dim, 1)
        self.pos = np.maximum(self.pos, mins)
        self.pos = np.minimum(self.pos, maxs)

    # --------------------------------------------------------
    def step(self):
        ids = np.random.randint(0, self.dirs.shape[1], self.num)
        moves = self.dirs[:, ids]
        self.pos += moves

        if self.is_limited:
            self._push_into_bounds()

    # --------------------------------------------------------
    def msteps(self, m):
        for _ in range(m):
            self.step()

    # --------------------------------------------------------
    def project_to_2d(self):
        """
        Проєкція n-вимірного простору на площину.
        Використовуємо перші дві координати.
        """
        if self.dim == 1:
            return np.vstack([self.pos[0], np.zeros(self.num)])
        return self.pos[:2]


# ============================================================
#                  Drunkard2D — нащадок ND
# ============================================================
class Drunkard2D(DrunkardND):
    """
    Двовимірний варіант моделі (повністю сумісний зі старим кодом).
    """

    def __init__(self, num_drunkards, init_pos=None,
                 is_limited=False, bounds=None):

        super().__init__(num_drunkards,
                         dim=2,
                         init_pos=init_pos,
                         is_limited=is_limited,
                         bounds=bounds)

    def plot(self):
        pos = self.project_to_2d()
        plt.scatter(pos[0], pos[1], s=20)
        if self.bounds:
            xmin, ymin = self.bounds[0]
            xmax, ymax = self.bounds[1]
            plt.xlim(xmin, xmax)
            plt.ylim(ymin, ymax)
        plt.grid(True)


# ============================================================
#                   Анімація одного газу
# ============================================================
def animate_drunkards(model, steps=200, interval=50):
    fig, ax = plt.subplots(figsize=(6, 6))

    def update(frame):
        ax.clear()
        model.step()
        pos = model.project_to_2d()
        ax.scatter(pos[0], pos[1], s=15)

        if model.bounds:
            xmin, ymin = model.bounds[0]
            xmax, ymax = model.bounds[1]
            ax.set_xlim(xmin, xmax)
            ax.set_ylim(ymin, ymax)

        ax.set_title(f"Step {frame}")

    # ------- ВАЖЛИВО!!! ----------
    ani = animation.FuncAnimation(
        fig, update, frames=steps, interval=interval
    )
    # зберігаємо у глобальну змінну, щоб Python не видалив
    globals()['_ani'] = ani
    # -----------------------------

    plt.show()

# ============================================================
#                   Анімація двох газів
# ============================================================
def animate_two_gases(model1, model2, steps=200, interval=50):
    fig, ax = plt.subplots(figsize=(6, 6))

    def update(frame):
        ax.clear()
        model1.step()
        model2.step()

        pos1 = model1.project_to_2d()
        pos2 = model2.project_to_2d()

        ax.scatter(pos1[0], pos1[1], s=15, color='blue')
        ax.scatter(pos2[0], pos2[1], s=15, color='red')

        if model1.bounds:
            xmin, ymin = model1.bounds[0]
            xmax, ymax = model1.bounds[1]
            ax.set_xlim(xmin, xmax)
            ax.set_ylim(ymin, ymax)

        ax.set_title(f"Step {frame}")

    # ---------- ВАЖЛИВО ----------
    ani = animation.FuncAnimation(
        fig, update, frames=steps, interval=interval
    )
    globals()['_ani'] = ani
    # ------------------------------

    plt.show()

# ============================================================
#               ПРИКЛАДИ ЗАПУСКУ (можеш забрати)
# ============================================================
if __name__ == "__main__":

    print("Запуск тестової анімації DrunkardND...")

    # Границі — навіть 2D bounds працює для ND
    bounds = [[0, 0], [200, 200]]

    # ----- Одне хмарино молекул у 5D -----
    modelND = DrunkardND(num_drunkards=120,
                         dim=5,
                         is_limited=True,
                         bounds=bounds)
    # animate_drunkards(modelND, 300, 30)

    # ----- Два гази (T20.31) -----
    init1 = np.zeros((2, 50))
    init1[0] = np.random.uniform(10, 80, 50)
    init1[1] = np.random.uniform(20, 180, 50)

    init2 = np.zeros((2, 50))
    init2[0] = np.random.uniform(120, 190, 50)
    init2[1] = np.random.uniform(20, 180, 50)

    A = Drunkard2D(50, init_pos=init1, is_limited=True, bounds=bounds)
    B = Drunkard2D(50, init_pos=init2, is_limited=True, bounds=bounds)

    # animate_two_gases(A, B, steps=300, interval=30)
