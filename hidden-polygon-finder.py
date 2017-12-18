import time

from polygon_same_name_generator import get_same_names_of_polygon
from shape_data import ShapeData


def main():
    wanted_polygon = list()
    shape_data = ShapeData("shape_metadata.yaml")
    straight_points = shape_data.get("straight_points")
    polygon_connected_points = shape_data.get("connected_points")
    wanted_polygon_points = shape_data.get("wanted_polygon_points")
    for points in straight_points:
        for point in points:
            linked_points = list(points)
            linked_points.remove(point)
            polygon_connected_points[point] += linked_points
            polygon_connected_points[point] = sorted(list(set(polygon_connected_points[point])))
    for point in polygon_connected_points:
        list_path = find_polygon(point, polygon_connected_points[point], polygon_connected_points,
                                 wanted_polygon_points - 1)
        new_path = list()
        for path in list_path:
            if point not in path:
                new_path.append(point + path)
        wanted_polygon += new_path

    path_have_no_straight_points = list(wanted_polygon)

    # Remove paths have 3 or more straight points
    for pol in wanted_polygon:
        for points in straight_points:
            count = 0
            if len(points) >= 3:
                for point in points:
                    if point in pol:
                        count += 1
                    if count >= 3:
                        path_have_no_straight_points.remove(pol)
                        break
    hidden_polygons = list(path_have_no_straight_points)
    ignored_polygons = list()
    for path in path_have_no_straight_points:
        if path in ignored_polygons:
            continue
        first_point = path[0]
        last_point = path[-1]
        same_name_polygons = get_same_names_of_polygon(path)
        # Remove same names of polygon
        hidden_polygons = [x for x in hidden_polygons if x not in same_name_polygons]
        ignored_polygons += same_name_polygons
        # Remove invalid path
        if last_point not in polygon_connected_points[first_point]:
            hidden_polygons.remove(path)
    print(str("Found " + str(len(hidden_polygons))) + " polygons")
    [print(polygon) for polygon in hidden_polygons]


def find_polygon(point, connected_points, polygon_connected_points, wanted_polygon_points):
    if wanted_polygon_points == 1:
        direct_links = list(connected_points)
        if point in direct_links: direct_links.remove(point)
        return direct_links
    wanted_polygon = list()
    for point in connected_points:
        list_path = find_polygon(point, polygon_connected_points[point], polygon_connected_points,
                                 wanted_polygon_points - 1)
        new_path = list()
        for path in list_path:
            if point not in path:
                new_path.append(point + path)
        wanted_polygon += new_path
    return wanted_polygon


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print("Finished in " + str(end - start))
