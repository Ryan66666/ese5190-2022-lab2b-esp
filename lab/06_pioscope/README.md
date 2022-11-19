# Part6: Yuchen Wang Worked with Katrina Ji & Ryan Zhang

---
University of Pennsylvania, ESE 5190: Intro to Embedded Systems, Lab 2b

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

## Screenshot of I2C Traffic with PICOSCOP:

<img width="1082" alt="Screen Shot 2022-11-11 at 22 26 13" src="https://user-images.githubusercontent.com/105755054/201454238-e920eb79-c6d7-41d2-92c3-8fb67922b359.png">

---

## Modified Code Parts:

- change to the I2C pins (22)

```
const uint CAPTURE_PIN_BASE = 22;
const uint CAPTURE_PIN_COUNT = 2;
const uint CAPTURE_N_SAMPLES = 96;
const uint BOOT_PIN = 21;

```

- Disabled trigger

```
//pio_sm_exec(pio, sm, pio_encode_wait_gpio(trigger_level, trigger_pin));
logic_analyser_arm(pio, sm, dma_chan, capture_buf, buf_size_words, CAPTURE_PIN_BASE, false);
```

- Add loop
```
    PIO pio = pio0;
    uint sm = 0;
    uint dma_chan = 0;
    printf("Press BOOT PIN to Start Measure");
    logic_analyser_init(pio, sm, CAPTURE_PIN_BASE, CAPTURE_PIN_COUNT, 256.f);
while(1){
    if (gpio_get(BOOT_PIN) == 0){
    logic_analyser_arm(pio, sm, dma_chan, capture_buf, buf_size_words, CAPTURE_PIN_BASE, false);
    print_capture_buf(capture_buf, CAPTURE_PIN_BASE, CAPTURE_PIN_COUNT, CAPTURE_N_SAMPLES);
        }
    }
}
```
---

# Explain:

<img width="501" alt="Screen Shot 2022-11-18 at 14 15 55" src="https://user-images.githubusercontent.com/105755054/202784746-fb92f981-fe74-4799-99be-c2db7d1d2b91.png">

This section, we hae to modify the example code to monitor the I2C traffic, for doing that we can use the PIO function with pio0 and sm0. Each state machine, along with its supporting hardware, occupies approximately the same silicon area as a standard serial interface block, such as an SPI or I2C controller. However, PIO state machines can be configured and reconfigured dynamically to implement numerous different interfaces. Making state machines programmable in a software-like manner, rather than a fully configurable logic fabric like a CPLD, allows more hardware interfaces to be offered in the same cost and power envelope. This also presents a more familiar programming model, and simpler tool flow, to those who wish to exploit PIO’s full flexibility by programming it directly, rather than using a premade interface from the PIO library.
