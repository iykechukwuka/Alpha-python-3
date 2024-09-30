import numpy as np
result = np.random.choice([0, 1], size=5)  # Randomly selects 5 elements from [0, 1]
print(result)

import numpy as np
result = np.random.choice([0, 1])  # Randomly selects 0 or 1
print(result)

import numpy as np
result = np.random.choice([0, 1, 2, 3], size=3, replace=False)  # Randomly selects 3 distinct elements
print(result)

import numpy as np
result = np.random.choice([0, 1], size=5, p=[0.2, 0.8])  # 1 has an 80% chance, 0 has a 20% chance
print(result)
