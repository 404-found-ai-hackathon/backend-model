from multiprocessing import Process
from yolov5.detect import CVModel


WEIGHTS_PATH = "weights/vehicle.pt"
YOLOV_WEIGHTS_PATH = "weights/yolov5s.pt"
LEFT_VIDEO_PATH = "data/leftReady.MOV"
RIGHT_VIDEO_PATH = "data/rightReady.MOV"
TOP_VIDEO_PATH = "data/topReady.MOV"
BOTTOM_VIDEO_PATH = "data/bottomReady.MOV"
LEFT_ROAD_DATA = {
    "road": "left",
    "cars": 0
}
RIGHT_ROAD_DATA = {
    "road": "right",
    "cars": 0
}
TOP_ROAD_DATA = {
    "road": "top",
    "cars": 0
}
BOTTOM_ROAD_DATA = {
    "road": "bottom",
    "cars": 0
}


def run_model(
    data_template: dict, 
    data_path: str, 
    view_img: bool, 
    polygon_vertices: list, 
    weights_path: str,
    classes=[2, 3, 5, 7]
):
    CVModel(data_template).run(
        weights=weights_path, 
        source=data_path, 
        view_img=view_img, 
        polygon_vertices=polygon_vertices,
        classes=classes
    )


if __name__ == "__main__":
    left_process = Process(
        target=run_model, 
        args=(
            LEFT_ROAD_DATA, 
            LEFT_VIDEO_PATH, 
            True, 
            [(1, 495), (1060, 171), (1167, 196), (560, 694), (431, 693), (5, 573)], 
            WEIGHTS_PATH,
            [0]
        )
    )
    right_process = Process(
        target=run_model, 
        args=(
            RIGHT_ROAD_DATA, 
            RIGHT_VIDEO_PATH, 
            True, 
            [(747, 657), (2, 654), (2, 495), (701, 250), (787, 241), (847, 186), (929, 195), (945, 352), (811, 660)], 
            YOLOV_WEIGHTS_PATH
        )
    )
    top_process = Process(
        target=run_model, 
        args=(
            TOP_ROAD_DATA, 
            TOP_VIDEO_PATH, 
            True, 
            [(2, 628), (3, 555), (490, 318), (640, 291), (719, 214), (778, 212), (860, 264), (1276, 602), (1274, 646)],
            YOLOV_WEIGHTS_PATH
        )
    )
    bottom_process = Process(
        target=run_model,
        args=(
            BOTTOM_ROAD_DATA,
            BOTTOM_VIDEO_PATH, 
            True, 
            [(4,614), (19, 582), (596, 75), (734, 82), (957, 306), (1275, 562), (1276, 645)], 
            YOLOV_WEIGHTS_PATH
        )
    )

    left_process.start()
    right_process.start()
    top_process.start()
    bottom_process.start()

    left_process.join()
    right_process.join()
    top_process.join()
    bottom_process.join()
