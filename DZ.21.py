from PIL import Image


def resize_image(input_image_path, output_image_path, size):
    original_image = Image.open(input_image_path)
    width, height = original_image.size
    print(f'Оригинальный размер изображения - ', width, 'ширина x', height, 'высота')

    resized_image = original_image.resize(size)
    width, height = resized_image.size
    print(f'Измененный размер изображения - ', width, 'ширина x', height, 'высота')
    resized_image.show()
    resized_image.save(output_image_path)


if __name__ == '__main__':
    resize_image(input_image_path='test.jpg',
                 output_image_path='test_resize.jpg',
                 size=(1920, 1080))
