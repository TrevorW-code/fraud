<div align='center'>

# fraud
### Pronunciation: /frɔːd/ (FRAWD)

#### *Simplified Synthetic Data*

</div>

fraud is a python package designed to streamline synthetic data for finetuning machine learning models. 

When finetuning for a domain specific task (i.e. extracting medical using NER), data scarcity can quickly become a limiting factor. Data annotation is the ideal solution; however it is often expensive, time-consuming, and resource-intensive. 

Synthetic data offers an effective middle ground, enabling models to significantly enhance their performance by supplementing smaller datasets.

# Usage

Here's a basic example to get you started.

```python
import fraud as fr

synthetic_samples = fr.make_fake('Could you please meet {name} at {time}', 20)
```