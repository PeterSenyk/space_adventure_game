import boards


def training_space():
    training_area = {
                    (0, 0): [1, "You're in the docking bay of the Arc-Corp training academy"],
                    (1, 0): [2, "You're in an empty grid in the training zone, take a moment to breathe."],
                    (0, 1): [3, "The training combat area is outlined by a ring of bright lights."],
                    (1, 1): [2, "You're in an empty grid in the training zone, take a moment to breathe."],
                    (0, 2): [3, "The training combat area is outlined by a ring of bright lights."],
                    (1, 2): [3, "The training combat area is outlined by a ring of bright lights."],
                    }
    return training_area


def outlaw_space():
    outlaw_area = {
                    (0, 0): [1, "You're in the docking bay of the Arc-Corp training academy"],
                    (1, 0): [2, "You're in an empty grid in the training zone, take a moment to breathe."],
                    (2, 3): [3, "The training combat area is outlined by a ring of bright lights."],
                    (0, 1): [2, "You're in an empty grid in the training zone, take a moment to breathe."],
                    (1, 1): [3, "The training combat area is outlined by a ring of bright lights."],
                    (2, 1): [3, "The training combat area is outlined by a ring of bright lights."],
                    (0, 2): [2, "You're in an empty grid in the training zone, take a moment to breathe."],
                    (1, 2): [3, "The training combat area is outlined by a ring of bright lights."],
                    (2, 2): [3, "The training combat area is outlined by a ring of bright lights."]
                    }
    return outlaw_area


def random_space():
    random_area = boards.make_space(10, 10)
    return random_area
