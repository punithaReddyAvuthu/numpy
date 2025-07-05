import numpy as np

sales_data = np.array([100,150,200,175,300])
print(f"Sales data:{sales_data}")
print(f"Type: {type(sales_data)}")
print(sales_data[-1])

monthly_sales = np.array([
    [100, 150,200],
    [160, 240, 169],
    [140, 170, 220]
])

print(monthly_sales[:, :2])

print(f"monthly sales shape: {monthly_sales.shape}")
print(f"size: {monthly_sales.size}")
print(f"dimensions: {monthly_sales.shape}")
print(f"data type: {monthly_sales.dtype}")

zeros_array = np.zeros(5);
one_array = np.ones((3,4))
range_array = np.arange(0, 12, 2)
linspace_array = np.linspace(0, 1, 5)

print(f"zeros: {zeros_array}")
print(f"Range: {range_array}")
print(f"linspace: {linspace_array}")


    

