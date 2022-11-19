# Part7 YuchenWang Worked with KatrinaJi & Ryan Zhang

---
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
    
## GIF of Reading Data from BOOT PIN with PIO and Write:


![IMG_9814](https://user-images.githubusercontent.com/105755054/202577162-845675b7-3a9a-4a9f-a98d-883c98b714e0.GIF)
![IMG_9815](https://user-images.githubusercontent.com/105755054/202577207-7c7b4d3a-a255-4cf1-ab69-43d831928658.GIF)

---

## Explain:

In this part, PIO has be used to read from BOOT PIN and write data to WS2812. The reference of this part is pio_scope(part6). Some code of this part had been modified:

- ``` void print_capture_buf () ```

```
void print_capture_buf(const uint32_t *buf, uint pin_base, uint pin_count, uint32_t n_samples) {
    uint record_size_bits = bits_packed_per_word(pin_count);
    for (int pin = 0; pin < pin_count; ++pin) {
        for (int sample = 0; sample < n_samples; ++sample) {
            uint bit_index = pin + sample * pin_count;
            uint word_index = bit_index / record_size_bits;
            if (buf[word_index] == 0){
                button_is_pressed = 0x1;
            }
            else{
                button_is_pressed = 0x0;
            }
        }
    }
}

```

- Add a function ``` void set_neopixel_color(uint32_t color) ``` in ``` WS2812.c ``` as API:

```
void set_neopixel_color(uint32_t color) {
    put_pixel(color);
}
```

---

## Note:

When I just slightly modify this example code, I find that this code can not read the BOOT PIN correctly, since I use the same PIO and SM for ws2812 and logic analyser simultaneously. It will introduce some errors when you it, so, I change the ws2812 with pio_0, logic analyser with pio_1, then this code will run correctly.
