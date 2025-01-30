<div align='center'>

# fraud
### Pronunciation: /frɔːd/ (FRAWD)

#### *Simplified Synthetic Data*

</div>

fraud is a python package designed to streamline synthetic data for finetuning machine learning models. 

Data scarcity is a limiting factor. While *real* data is the ideal solution; however it is often expensive, time-consuming, and resource-intensive. 

Synthetic data offers an effective middle ground, enabling models to significantly enhance their performance by supplementing smaller datasets.

# Usage

Here's a basic example to get you started.

```python
import fraud as fr

synthetic_samples = fr.from_str('Could you please meet {name} at {time}', 20)
```

# Predicting Templates

Grab a sample from your dataset to make a template from it!

```python
import fraud as fr

predicted_template = fr.predict_template(
    sample='My name is Trevor and I am a Data Scientist.',
    labels=['name','job'],
    threshold=0.5
)

fr.from_str(predicted_template, 5)
```