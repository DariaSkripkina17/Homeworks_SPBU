import math
from abc import ABC, abstractmethod
class Location:
    """
    Класс Location представляет собой местоположение с определенными габаритами (ширина, высота, длина).
    В данном местоположении могут располагаться объекты.

    Методы класса позволяют добавлять объекты, проверять, находятся ли координаты внутри границ местоположения,
    а также получать информацию о его размерах.
    """

    def __init__(self, name: str, width: int, height: int, length: int):
        """
        Инициализация нового объекта Location.

        Параметры:
        - name: str - Имя местоположения.
        - width: int - Ширина местоположения.
        - height: int - Высота местоположения.
        - length: int - Длина местоположения.
        """
        self.name = name  # Имя местоположения
        self._width = width  # Ширина
        self._height = height  # Высота
        self._length = length  # Длина
        self._objs = []  # Список объектов в данном местоположении

    def addObject(self, obj):
        """
        Добавляет объект в список объектов местоположения.

        Параметры:
        - obj: GameObject - Объект, который добавляется в местоположение.
        """
        if obj not in self._objs:
            self._objs.append(obj)

    def clear(self):
        """Очищает список объектов в местоположении."""
        self._objs = None

    def isInside(self, x, y, z) -> bool:
        """
        Проверяет, находятся ли указанные координаты внутри границ местоположения.

        Параметры:
        - x, y, z: int - Координаты для проверки.

        Возвращает:
        - bool - True, если координаты внутри границ местоположения, False в противном случае.
        """
        return ((x > 0 and x < self._length)
                and (y > 0 and y < self._width)
                and (z > 0 and z < self._height))

    @property
    def width(self):
        """Свойство, возвращающее ширину местоположения."""
        return self._width

    @property
    def length(self) -> int:
        """Свойство, возвращающее длину местоположения."""
        return self._length

    @property
    def height(self):
        """Свойство, возвращающее высоту местоположения."""
        return self._height

    @property
    def volume(self):
        """Свойство, возвращающее объем местоположения."""
        return self.height * self.length * self.width


class GameObject:
    """
    Класс GameObject представляет объект в трехмерном пространстве с координатами x, y, z.
    Он также связан с местоположением (Location), в котором находится объект.
    """

    def __init__(self, name: str, loc: Location, x, y, z):
        """
        Инициализация нового объекта GameObject.

        Параметры:
        - name: str - Имя объекта.
        - loc: Location - Местоположение, где находится объект.
        - x, y, z - Начальные координаты объекта в трехмерном пространстве.
        """
        self.name = name  # Имя объекта
        self._loc = loc  # Ссылка на местоположение (объект типа Location), где находится объект
        self._loc.addObject(self)  # Добавление объекта в список объектов местоположения
        self.x, self.y, self.z = x, y, z  # Установка начальных координат объекта

    @property
    def x(self):
        """Свойство, возвращающее текущую координату x."""
        return self._x

    @x.setter
    def x(self, x):
        """
        Устанавливает координату x с проверкой на выход за границы местоположения.

        Параметры:
        - x: int - Новое значение координаты x.
        """
        if x < 0:
            self._x = 0
        elif self._loc.length < x:
            self._x = self._loc.length
        else:
            self._x = x

    @property
    def y(self):
        """Свойство, возвращающее текущую координату y."""
        return self._y

    @y.setter
    def y(self, y):
        """
        Устанавливает координату y с проверкой на выход за границы местоположения.

        Параметры:
        - y: int - Новое значение координаты y.
        """
        if y < 0:
            self._y = 0
        elif self._loc.width < y:
            self._y = self._loc.width
        else:
            self._y = y

    @property
    def z(self):
        """Свойство, возвращающее текущую координату z."""
        return self._z

    @z.setter
    def z(self, z):
        """
        Устанавливает координату z с проверкой на выход за границы местоположения.

        Параметры:
        - z: int - Новое значение координаты z.
        """
        if z < 0:
            self._z = 0
        elif self._loc.height < z:
            self._z = self._loc.height
        else:
            self._z = z

    def move(self, x, y, z):
        """
        Перемещает объект на указанные величины по осям x, y, z.

        Параметры:
        - x, y, z: int - Величины изменения координат.
        """
        self.x += x
        self.y += y
        self.z += z

    def distance(self, obj):
        """
        Вычисляет расстояние между текущим объектом и другим объектом obj в трехмерном пространстве.

        Параметры:
        - obj: GameObject - Другой объект, до которого измеряется расстояние.

        Возвращает:
        - int - Целочисленное значение расстояния.
        """
        dx = self.x - obj.x
        dy = self.y - obj.y
        dz = self.z - obj.z
        r2 = dx ** 2 + dy ** 2 + dz ** 2
        return int(math.sqrt(r2))  # Возвращает целочисленное значение расстояния


class LivingObject(GameObject):
    """
    Класс LivingObject представляет собой живой объект, являющийся наследником класса GameObject.
    Этот класс добавляет характеристики здоровья, инвентаря, кровотечения и методы для работы с ними.
    """

    def __init__(self, name: str, loc: Location, x, y, z, hp: int):
        """
        Инициализация нового живого объекта LivingObject.

        Параметры:
        - name: str - Имя живого объекта.
        - loc: Location - Местоположение, где находится объект.
        - x, y, z: int - Начальные координаты объекта в трехмерном пространстве.
        - hp: int - Начальное количество здоровья объекта.
        """
        super().__init__(name, loc, x, y, z)  # Вызов конструктора родительского класса
        self._max_hp = hp  # Максимальное количество здоровья
        self._hp = hp  # Текущее количество здоровья
        self._bleeding = 0  # Уровень кровотечения
        self._inventory = []  # Инвентарь

    @property
    def inventory(self):
        """
        Свойство, возвращающее инвентарь живого объекта.

        Возвращает:
        - list - Список предметов в инвентаре.
        """
        return self._inventory

    def pickUpItem(self, item):
        """
        Подбирает предмет и добавляет его в инвентарь.

        Параметры:
        - item: Eatable - Предмет, который поднимается.
        """
        if item not in self._inventory:
            self._inventory.append(item)
            item.pickUp(self)  # Вызываем метод pickUp у предмета, чтобы он выполнил действия при подборе

    def useItem(self, item):
        """
        Использует предмет из инвентаря.

        Параметры:
        - item: Eatable - Предмет, который используется.
        """
        if item in self._inventory:
            item.use(self)  # Вызываем метод use у предмета, чтобы он выполнил действия при использовании

    @property
    def maxHP(self):
        """Свойство, возвращающее максимальное количество здоровья."""
        return self._max_hp

    @property
    def hp(self):
        """Свойство, возвращающее текущее количество здоровья."""
        return self._hp

    def changeHP(self, change):
        """
        Изменяет количество здоровья объекта на указанную величину.

        Параметры:
        - change: int - Величина изменения здоровья.
        """
        if not self.alive:  # Если объект мертв, игнорируем изменение здоровья
            return
        self._hp += change
        if self._hp < 0:  # Здоровье не может быть отрицательным
            self._hp = 0
        if self._hp > self._max_hp:  # Здоровье не может превышать максимальное значение
            self._hp = self._max_hp

    @property
    def alive(self):
        """
        Свойство, определяющее, жив ли объект.

        Возвращает:
        - bool - True, если объект жив, False в противном случае.
        """
        return self._hp > 0

    def eat(self, obj):
        """
        Пытается выполнить действие поедания другого объекта.

        Параметры:
        - obj: GameObject - Объект, который пытается быть съеденным.
        """
        if self.distance(obj) > 1:  # Если объект слишком далеко, не выполняем действие
            return
        self.changeHP(obj.eatMe())  # Вызываем метод eatMe() у другого объекта и изменяем здоровье текущего объекта

    @property
    def bleeding(self):
        """Свойство, возвращающее уровень кровотечения."""
        return self._bleeding

    def changeBleeding(self, change):
        """
        Изменяет уровень кровотечения объекта на указанную величину.

        Параметры:
        - change: int - Величина изменения уровня кровотечения.
        """
        self._bleeding += change
        self.changeHP(-change)  # Уменьшаем здоровье на величину кровотечения


class Weapon(GameObject):
    """
    Класс Weapon представляет собой оружие, являющееся наследником класса GameObject.
    Оружие обладает характеристиками урона и радиуса действия, а также методом для выполнения атаки.
    """

    def __init__(self, name: str, loc: Location, x, y, z, damage, radius):
        """
        Инициализация нового объекта Weapon.

        Параметры:
        - name: str - Имя оружия.
        - loc: Location - Местоположение, где находится оружие.
        - x, y, z: int - Начальные координаты оружия в трехмерном пространстве.
        - damage: int - Величина урона, наносимого оружием.
        - radius: int - Радиус действия оружия.
        """
        super().__init__(name, loc, x, y, z)  # Вызов конструктора родительского класса
        self._damage = damage  # Величина урона
        self._radius = radius  # Радиус действия

    @property
    def damage(self):
        """
        Свойство, возвращающее величину урона оружия.

        Возвращает:
        - int - Величина урона.
        """
        return self._damage

    @property
    def radius(self):
        """
        Свойство, возвращающее радиус действия оружия.

        Возвращает:
        - int - Радиус действия.
        """
        return self._radius

    def attack(self, obj: LivingObject):
        """
        Выполняет атаку по живому объекту в радиусе действия оружия.

        Параметры:
        - obj: LivingObject - Живой объект, который является целью атаки.
        """
        d = self.distance(obj)  # Расстояние между оружием и целью
        if d > self.radius:  # Если цель слишком далеко, не выполняем атаку
            return
        obj.changeHP(-self.damage)  # Уменьшаем здоровье цели на величину урона оружия


class ColdWeapon(Weapon):
    """
    Класс ColdWeapon представляет собой холодное оружие, являющееся подклассом класса Weapon.
    Холодное оружие имеет дополнительный эффект - кровотечение, который оказывается на живой объект при успешной атаке.
    """

    def __init__(self, name: str, loc: Location, x, y, z, damage, radius, bleeding_damage):
        """
        Инициализация нового объекта ColdWeapon.

        Параметры:
        - name: str - Имя холодного оружия.
        - loc: Location - Местоположение, где находится холодное оружие.
        - x, y, z: int - Начальные координаты холодного оружия в трехмерном пространстве.
        - damage: int - Величина урона, наносимого холодным оружием.
        - radius: int - Радиус действия холодного оружия.
        - bleeding_damage: int - Величина урона от кровотечения.
        """
        super().__init__(name, loc, x, y, z, damage, radius)  # Вызов конструктора родительского класса
        self._bleeding_damage = bleeding_damage  # Величина урона от кровотечения

    @property
    def bleeding_damage(self):
        """
        Свойство, возвращающее величину урона от кровотечения холодного оружия.

        Возвращает:
        - int - Величина урона от кровотечения.
        """
        return self._bleeding_damage

    def cause_bleeding(self, obj: LivingObject):
        """
        Наносит урон от кровотечения живому объекту в радиусе действия холодного оружия.

        Параметры:
        - obj: LivingObject - Живой объект, который является целью кровотечения.
        """
        d = self.distance(obj)  # Расстояние между холодным оружием и целью
        if d > self.radius:  # Если цель слишком далеко, не наносим урон от кровотечения
            return
        obj.changeBleeding(self.bleeding_damage)  # Вызываем метод changeBleeding у цели


class ThrowingWeapon(Weapon):
    """
    Класс ThrowingWeapon представляет собой метательное оружие, являющееся подклассом класса Weapon.
    Метательное оружие обладает методом для выполнения метания в определенном направлении.
    """

    def __init__(self, name: str, loc: Location, x, y, z, damage, radius):
        """
        Инициализация нового объекта ThrowingWeapon.

        Параметры:
        - name: str - Имя метательного оружия.
        - loc: Location - Местоположение, где находится метательное оружие.
        - x, y, z: int - Начальные координаты метательного оружия в трехмерном пространстве.
        - damage: int - Величина урона, наносимого метательным оружием.
        - radius: int - Радиус действия метательного оружия.
        """
        super().__init__(name, loc, x, y, z, damage, radius)  # Вызов конструктора родительского класса

    def throw_on_direction(self, angle: float, radius: float):
        """
        Выполняет метание в определенном направлении.

        Параметры:
        - angle: float - Угол (в радианах), в направлении которого выполняется метание.
        - radius: float - Расстояние, на которое происходит метание.
        """
        # Преобразование полярных координат в декартовы координаты
        target_x = self.x + radius * math.cos(angle)
        target_y = self.y + radius * math.sin(angle)
        target_z = self.z  # Предполагаем, что метательное оружие стреляет в плоскости XY

        # Вывод сообщения о выполнении выстрела
        print(f"{self.name} выполнил выстрел в направлении {math.degrees(angle)} градусов.")


class Eatable(ABC):
    """
    Класс Eatable представляет собой абстрактный класс для объектов, которые могут быть съедены.
    """

    def __init__(self, hp: int):
        """
        Инициализация нового объекта Eatable.

        Параметры:
        - hp: int - Количество здоровья, которое может восстановиться при съедении.
        """
        self._hp = hp  # Количество здоровья
        self._eaten = False  # Флаг, указывающий, был ли объект съеден

    @property
    def eaten(self):
        """
        Свойство, возвращающее значение флага, был ли объект съеден.

        Возвращает:
        - bool - True, если объект был съеден, False в противном случае.
        """
        return self._eaten

    @abstractmethod
    def eatMe(self, eater):
        """
        Абстрактный метод, который должен быть реализован в подклассах.
        Выполняет действие съедения объекта.

        Параметры:
        - eater: LivingObject - Объект, который съедает текущий объект.

        Возвращает:
        - int - Количество здоровья, которое восстанавливается при съедении.
        """
        if not self.eaten:
            self._eaten = True  # Устанавливаем флаг, что объект был съеден
            return self._hp  # Возвращаем количество здоровья, которое восстанавливается при съедении
        else:
            return 0  # Если объект уже был съеден, возвращаем 0 здоровья


class Food(GameObject, Eatable):
    """
    Класс Food представляет собой объект еды, являющийся наследником классов GameObject и Eatable.
    Этот класс объединяет функциональность объекта в игровом мире и возможность быть съеденным.
    """

    def __init__(self, name, loc, x, y, z, hp):
        """
        Инициализация нового объекта Food.

        Параметры:
        - name: str - Имя еды.
        - loc: Location - Местоположение, где находится еда.
        - x, y, z: int - Начальные координаты еды в трехмерном пространстве.
        - hp: int - Количество здоровья, которое восстанавливается при съедении.
        """
        GameObject.__init__(self, name, loc, x, y, z)  # Вызов конструктора родительского класса GameObject
        Eatable.__init__(self, hp)  # Вызов конструктора родительского класса Eatable

    def eatMe(self, eater):
        """
        Реализация метода eatMe для объекта еды.

        Параметры:
        - eater: LivingObject - Объект, который съедает еду.

        Возвращает:
        - int - Количество здоровья, которое восстанавливается при съедении.
        """
        hp = -super().eatMe(eater)  # Используем метод eatMe из класса Eatable
        eater.changeHP(hp)  # Изменяем здоровье объекта, который съедает еду

    def pickUp(self, eater):
        """
        Метод для подбора еды.

        Параметры:
        - eater: LivingObject - Объект, который поднимает еду.
        """
        eater.pickUpItem(self)  # Вызываем метод pickUpItem у объекта, который поднимает еду


class Poison(GameObject, Eatable):
    """
    Класс Poison представляет собой объект, представляющий яд, являющийся наследником классов GameObject и Eatable.
    Этот класс объединяет функциональность объекта в игровом мире и возможность быть съеденным, но с отрицательным эффектом.
    """

    def __init__(self, name, loc, x, y, z, hp):
        """
        Инициализация нового объекта Poison.

        Параметры:
        - name: str - Имя яда.
        - loc: Location - Местоположение, где находится яд.
        - x, y, z: int - Начальные координаты яда в трехмерном пространстве.
        - hp: int - Количество здоровья, которое теряется при съедении яда.
        """
        GameObject.__init__(self, name, loc, x, y, z)  # Вызов конструктора родительского класса GameObject
        Eatable.__init__(self, hp)  # Вызов конструктора родительского класса Eatable

    def eatMe(self, eater):
        """
        Реализация метода eatMe для объекта яда.

        Параметры:
        - eater: LivingObject - Объект, который съедает яд.

        Возвращает:
        - int - Количество здоровья, которое теряется при съедении яда.
        """
        hp = -Eatable.eatMe(eater)  # Используем метод eatMe из класса Eatable
        eater.changeHP(hp)  # Изменяем здоровье объекта, который съедает яд

    def pickUp(self, eater):
        """
        Метод для подбора яда.

        Параметры:
        - eater: LivingObject - Объект, который поднимает яд.
        """
        eater.pickUpItem(self)  # Вызываем метод pickUpItem у объекта, который поднимает яд


class Burnable(ABC):
    """
    Класс Burnable представляет собой абстрактный класс для объектов, которые могут быть подвергнуты воздействию огня.
    """

    def __init__(self):
        """
        Инициализация нового объекта Burnable.
        """
        self._burned = False  # Флаг, указывающий, был ли объект подвергнут воздействию огня

    @property
    def burned(self):
        """
        Свойство, возвращающее значение флага, был ли объект подвергнут воздействию огня.

        Возвращает:
        - bool - True, если объект был подвергнут воздействию огня, False в противном случае.
        """
        return self._burned

    @abstractmethod
    def burnMe(self, burner):
        """
        Абстрактный метод, который должен быть реализован в подклассах.
        Выполняет действие поджигания объекта.

        Параметры:
        - burner: GameObject - Объект, который поджигает текущий объект.
        """
        self._burned = True  # Устанавливаем флаг, что объект был подвергнут воздействию огня


class Cookable(GameObject, Eatable, Burnable):
    """
    Класс Cookable представляет собой объект, который можно приготовить, являющийся наследником классов
    GameObject, Eatable и Burnable. Объект может быть съеден, подвергнут воздействию огня и приготовлен.
    """

    def __init__(self, name, loc, x, y, z, hp):
        """
        Инициализация нового объекта Cookable.

        Параметры:
        - name: str - Имя объекта, который можно приготовить.
        - loc: Location - Местоположение, где находится объект.
        - x, y, z: int - Начальные координаты объекта в трехмерном пространстве.
        - hp: int - Количество здоровья, которое восстанавливается при съедении или приготовлении.
        """
        GameObject.__init__(self, name, loc, x, y, z)  # Вызов конструктора родительского класса GameObject
        Eatable.__init__(self, hp)  # Вызов конструктора родительского класса Eatable
        Burnable.__init__(self)  # Вызов конструктора родительского класса Burnable

    @classmethod
    def growMushroom(cls, loc, x, y, z):
        """
        Метод класса, создающий объект "гриб" на указанных координатах.

        Параметры:
        - loc: Location - Местоположение, где должен появиться гриб.
        - x, y, z: int - Координаты места появления гриба.

        Возвращает:
        - Cookable - Экземпляр класса Cookable с именем 'mushroom' и начальными координатами.
        """
        return cls('mushroom', loc, x, y, z, 20)  # Создаем объект "гриб" с начальными параметрами

    def burnMe(self, burner):
        """
        Реализация метода burnMe для объекта, который можно приготовить.

        Параметры:
        - burner: GameObject - Объект, который поджигает текущий объект.
        """
        Burnable.burnMe(burner)  # Вызываем метод burnMe из класса Burnable

    def eatMe(self, eater):
        """
        Реализация метода eatMe для объекта, который можно приготовить.

        Параметры:
        - eater: LivingObject - Объект, который съедает текущий объект.
        """
        hp = Eatable.eatMe(eater)  # Вызываем метод eatMe из класса Eatable
        if self.burned:
            eater.changeHP(hp)  # Если объект приготовлен, восстанавливаем здоровье объекта, который съедает
        else:
            eater.pickUpItem(self)  # Иначе, поднимаем объект, который съедает