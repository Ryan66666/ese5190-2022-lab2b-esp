# Part4 YuchenWang Worked with KatrinaJi & Ryan Zhang

---
# GIF of 2X Input with Duration of 5 sec

![IMG_9802](https://user-images.githubusercontent.com/105755054/202316319-907d265c-0d42-40bf-bef3-64c774805ace.GIF)
![IMG_9803](https://user-images.githubusercontent.com/105755054/202316322-e6ec8006-c0b3-42e2-b2f7-6e75753967b3.GIF)

The output should be 2.5s

# GIF of 0.5X Output With Duration of 5 sec


![IMG_9806](https://user-images.githubusercontent.com/105755054/202317288-ab0ef5e0-8500-42e6-8abc-7eb2aeba31d5.GIF)
![IMG_9807](https://user-images.githubusercontent.com/105755054/202317293-60eea9e9-6bc7-4b84-9bdc-fb48bd08fbd6.GIF)


The output should be 10 s

---

## Explain 

In this part we only need to add two functions at Python to achieve control the motion.

- `slow_motion`  funtion

```
def slow_motion(data_arrays):
    two_times_data = []
    for data in data_arrays:
        two_times_data.append(data)
        two_times_data.append(data)
    return two_times_data
```

This function inserts a same array to the orinal array with 1 bit position shift. For example, if I input 10, I will insert the bits as follwing next positions and it will become 1100. So, when my input rate is 1X and the duration is 5 seconds, my output is 0.5X and the duration will be 10 seconds.

---

- `up_motion` function

```
def up_motion(data_arrays):
    half_data = []
    for index in range(len(data_arrays)):
        if index % 2 == 0:
            half_data.append(data_arrays[index])
    return half_data
```

This function removes the odd or even bits of the entire record to halve the data. For example, if I input 1100, I will remove the bits on even positions and it will become 10. So, when my input rate is 1X and the duration is 5 seconds, my output is 2X and the duration will be 2.5 seconds.

