# Part8-YuchenWang-Worked-with-KatrinaJi & Ryan Zhang
University of Pennsylvania, ESE 5190: Intro to Embedded Systems, Lab 2b

### Teammate: Yuchen Wang, Katrina Ji

    Yuchen Wang
    wangyuchen0303@gmail.com
    Tested on:  MacBook Pro (14-inch, 2021), macOS Monterey 12.6
    
    Katrina Ji
    katji@seas.upenn.edu
    Tested on:  MacBook Pro (14-inch, 2021), macOS Monterey 12.6
    
    Ryan Zhang
    zcy6@seas.upenn.edu
    Tested on: Lenovo Legoin R900X
    
---

# Reference Note:

In this section we have adopt some code from classmates which I will list below:
- user name: Dang0V
  
  https://github.com/Dang0v/ese5190-2022-lab2b-esp.git 
  
- user name: TomGoh
  
  https://github.com/TomGoh/ese_5190_lab2b.git
  
- user name: HaoliangYou
  
  https://github.com/HaoliangYou/ese5190-2022-lab2b-esp.git
  
---

# GIF of Output:

![IMG_9821](https://user-images.githubusercontent.com/105755054/202827052-57d2c8e1-bac5-4966-bb23-a6cc0c027970.GIF)

---
# Modified Parts:

- define two functions to read 
```
init_sensor();
proximity_sensor(&proximity, pio, sm, address, true);
```
- thses two functions are adopt from the users post above:

```
void proximity_sensor(int32_t *proximity, PIO pio, uint sm, uint32_t addr, bool continue_do){
    uint8_t buf[1];
    uint8_t reg = PDATA_REG;
    pio_i2c_write_blocking(pio, sm, addr, &reg, 1, continue_do);  // true to keep master control of bus
    pio_i2c_read_blocking(pio, sm, addr, buf, 1, false);  // false - finished with bus

    *proximity = buf[0];
}

void read_rgbc(int32_t* r, int32_t* g, int32_t* b, int32_t* c) {

    uint8_t buf[2];
    uint8_t reg = CDATA_REG_L;
    pio_i2c_write_blocking(pio, sm, addr, &reg, 1, true);  // true to keep master control of bus
    pio_i2c_read_blocking(pio, sm, addr, buf, 8, false);  // false - finished with bus

    *c = (buf[1] << 8) | buf[0];
    *r = (buf[3] << 8) | buf[2];
    *g = (buf[5] << 8) | buf[4];
    *b = (buf[7] << 8) | buf[6];
}

```

- Modify the ```i2c.c``` and ```i2c.pio```
```
int pio_i2c_write_blocking(PIO pio, uint sm, uint8_t addr, uint8_t *txbuf, uint len, bool nonstop) {
    int err = 0;
    pio_i2c_start(pio, sm);
    pio_i2c_rx_enable(pio, sm, false);
    pio_i2c_put16(pio, sm, (addr << 2) | 1u);
    while (len && !pio_i2c_check_error(pio, sm)) {
        if (!pio_sm_is_tx_fifo_full(pio, sm)) {
            --len;
            pio_i2c_put_or_err(pio, sm, (*txbuf++ << PIO_I2C_DATA_LSB) | ((len == 0) << PIO_I2C_FINAL_LSB) | 1u);
        }
    }
    if (!nonstop)
        pio_i2c_stop(pio, sm);
    pio_i2c_wait_idle(pio, sm);
    if (pio_i2c_check_error(pio, sm)) {
        err = -1;
        pio_i2c_resume_after_error(pio, sm);
        pio_i2c_stop(pio, sm);
    }
    return err;
}

int pio_i2c_read_blocking(PIO pio, uint sm, uint8_t addr, uint8_t *rxbuf, uint len, bool nostop) {
    int err = 0;
    pio_i2c_repstart(pio, sm);
    pio_i2c_rx_enable(pio, sm, true);
    while (!pio_sm_is_rx_fifo_empty(pio, sm))
        (void)pio_i2c_get(pio, sm);
    pio_i2c_put16(pio, sm, (addr << 2) | 3u);
    uint32_t tx_remain = len; // Need to stuff 0xff bytes in to get clocks

    bool first = true;

    while ((tx_remain || len) && !pio_i2c_check_error(pio, sm)) {
        if (tx_remain && !pio_sm_is_tx_fifo_full(pio, sm)) {
            --tx_remain;
            pio_i2c_put16(pio, sm, (0xffu << 1) | (tx_remain ? 0 : (1u << PIO_I2C_FINAL_LSB) | (1u << PIO_I2C_NAK_LSB)));
        }
        if (!pio_sm_is_rx_fifo_empty(pio, sm)) {
            if (first) {
                // Ignore returned address byte
                (void)pio_i2c_get(pio, sm);
                first = false;
            }
            else {
                --len;
                *rxbuf++ = pio_i2c_get(pio, sm);
            }
        }
    }
    pio_i2c_stop(pio, sm);
    pio_i2c_wait_idle(pio, sm);
    if (pio_i2c_check_error(pio, sm)) {
        err = -1;
        pio_i2c_resume_after_error(pio, sm);
        pio_i2c_stop(pio, sm);
    }
    return err;
}
```

<img width="647" alt="Screen Shot 2022-11-18 at 21 27 52" src="https://user-images.githubusercontent.com/105755054/202830114-cfa44000-b3ed-4a10-afaa-aba6f5de9e6d.png">


---
# Explain:

The addresses definded in ``` adps.h``` can be find at ADPS9960 datasheet

<img width="647" alt="Screen Shot 2022-11-18 at 21 08 40" src="https://user-images.githubusercontent.com/105755054/202830152-764e1f28-5fba-412c-8a63-480e4deb2dcb.png">



