from typing import Any

from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.db import transaction


class Command(BaseCommand):
    help = "Очищает базу и загружает тестовые данные из фикстур"

    def add_arguments(self, parser: Any) -> Any:
        parser.add_argument(
            "--no-flush",
            action="store_true",
            help="Не очищать базу перед загрузкой",
        )

    def handle(self, *args: Any, **options: Any) -> Any:
        no_flush = options["no_flush"]

        with transaction.atomic():
            if not no_flush:
                self.stdout.write("Очистка базы данных...")
                call_command("flush", "--no-input")

            self.stdout.write("Загрузка тестовых данных...")

            # Загружаем категории
            try:
                call_command("loaddata", "categories")
                self.stdout.write(self.style.SUCCESS("Категории загружены"))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Ошибка загрузки категорий: {e}"))

            # Загружаем продукты
            try:
                call_command("loaddata", "catalog")
                self.stdout.write(self.style.SUCCESS("Продукты загружены"))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Ошибка загрузки продуктов: {e}"))

        self.stdout.write(self.style.SUCCESS("Все данные успешно загружены!"))
