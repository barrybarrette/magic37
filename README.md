# Magic #37
### Why is 37 significant in this weird niche case?

This project is the result of a conversation with a friend about the average probabilities of consecutive "combos" given a specified %chance to combo. Neither of us are mathematicians, but I will do my best to explain.

For example:
Given a 50% chance to combo (i.e. a coin flip), what is the average combo you'd get if you keep going until you lose?

This can be measured quite simply as shown in the `measure` function. We simply flip the "coin", and record the result. Repeating this `n` times gives us the answer of approximately `1` when the combo chance is 50%. Higher values of `n` increase the accuracy of the measurement but also significantly increase the time it takes to calculate at higher combo chance%.

I then began thinking of a way to approximate the measured result mathematically without having to measure `n` flips. I came up with the idea to just take the combo chance and multiply it against itself until we crossed some threshold. The only thing I didn't know going into this was what that threshold would be, or if there even would be a single static threshold that works universally. Enter the magic number `37`. What I found through testing is that if I multiply the combo chance by itself until the result was less than `37%` then I get a pretty close approximation of the measured result! Interestingly, the accuracy of this method actually gets better the higher the combo chance is. This is particularly interesting because as we increase the combo chance, the time it takes to measure high values of `n` increase significantly, making the approximation value far less intensive to compute versus measuring it.

Below you can see a sample result output from running on my computer. You can see that at low combo chance the variance is high, but as combo chance increases the computation becomes far more accurate while the time to measure the result inflates significantly.



| Combo Chance | Calculated Approximation | Measured Result | Time To Measure | n         |
|--------------|--------------------------|-----------------|-----------------|-----------|
| 50%          | 1.43                     | 1.00            | 1.7s            | 1,000,000 |
| 80%          | 4.46                     | 4.01            | 4.0s            | 1,000,000 |
| 85%          | 6.12                     | 5.67            | 5.1s            | 1,000,000 |
| 90%          | 9.44                     | 9.01            | 7.6s            | 1,000,000 |
| 95%          | 19.39                    | 18.99           | 15.1s           | 1,000,000 |
| 98%          | 49.22                    | 48.97           | 37.5s           | 1,000,000 |
| 99%          | 98.93                    | 98.99           | 1m14.6s         | 1,000,000 |

Is there any explanation for why 37 is the magic number here? Like I said at first, neither of us are mathematicians. Is this common knowledge among the mathematics community?
