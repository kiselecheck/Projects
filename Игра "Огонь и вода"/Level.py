import pygame as pg
from screen import bg


class Block(pg.sprite.Sprite):
    """Класс блоков"""
    def __init__(self, image_path: str):
        super().__init__()
        self.image = pg.image.load(image_path)
        self.rect = self.image.get_rect()


class Level:
    """
    Класс, который описывает, где будут находиться все блоки на определенном уровне игры
    """
    def __init__(self, level: list[str]):
        """Расшифровка входного файла с уровнем"""
        self.level = level
        # Размеры блоков
        block_width = 16
        block_height = 16
        #Создаем списки с элементами типа sprite для каждого блока
        self.platform_list = pg.sprite.Group()
        self.water_block_list = pg.sprite.Group()
        self.fire_block_list = pg.sprite.Group()
        self.dead_block_list = pg.sprite.Group()
        self.win_list = pg.sprite.Group()
        for row_idx, row in enumerate(level):   #проходимся по всем строкам
            for col_idx, col in enumerate(row):  #и всем элементам в строке
                if col == "-":
                    platform = Block('./photos/platform.png')
                    platform.rect.x = col_idx * block_width
                    platform.rect.y = row_idx * block_height
                    self.platform_list.add(platform)
                elif col == "W":
                    water_block = Block('sea/water3.png')
                    water_block.rect.x = col_idx * block_width
                    water_block.rect.y = row_idx * block_height
                    self.water_block_list.add(water_block)
                elif col == "w":
                    water_block = Block('sea/water_left2.png')
                    water_block.rect.x = col_idx * block_width
                    water_block.rect.y = row_idx * block_height
                    self.water_block_list.add(water_block)
                elif col == "V":
                    water_block = Block('sea/water_right2.png')
                    water_block.rect.x = col_idx * block_width
                    water_block.rect.y = row_idx * block_height
                    self.water_block_list.add(water_block)
                elif col == "F":
                    fire_block = Block('lava/lava.png')
                    fire_block.rect.x = col_idx * block_width
                    fire_block.rect.y = row_idx * block_height
                    self.fire_block_list.add(fire_block)
                elif col == "f":
                    fire_block = Block('lava/lava_left.png')
                    fire_block.rect.x = col_idx * block_width
                    fire_block.rect.y = row_idx * block_height
                    self.fire_block_list.add(fire_block)
                elif col == "P":
                    fire_block = Block('lava/lava_right.png')
                    fire_block.rect.x = col_idx * block_width
                    fire_block.rect.y = row_idx * block_height
                    self.fire_block_list.add(fire_block)
                elif col == "d":
                    dead_block = Block('./photos/slime.png')
                    dead_block.rect.x = col_idx * block_width
                    dead_block.rect.y = row_idx * block_height
                    self.dead_block_list.add(dead_block)
                elif col == "G":
                    win_block = Block('./photos/dom.png')
                    win_block.rect.x = col_idx * block_width
                    win_block.rect.y = row_idx * block_height
                    self.win_list.add(win_block)
        self.all_sprites = pg.sprite.Group(self.win_list, self.dead_block_list, self.fire_block_list,
                                           self.water_block_list, self.platform_list)  #   всё что надо рисовать

    def draw(self, screen: pg.surface.Surface):
        """
        Прорисовка всех объектов уровня
        """
        screen.blit(bg, (0, 0))  # Рисуем задний фон
        self.all_sprites.draw(screen)  # Рисуем все объекты из группы спрайтов
