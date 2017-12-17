# Hidden Polygon Finder
Find hidden polygon from input polygon metadata

## Instructions for input data

1. `wanted_polygon_points`: Total points of wanted polygon
2. `points`: List of points of input shape
3. `straight_points`: List of straight point collection
4. `connected_points`: Collection of direct connected points. (If shape has 3 ordered straight points A, B, C. So C and A don't connect directly).

## Run instruction

1. I assumed you have input data file.
2. Then run

```python
python hidden-polygon-finder.py
```