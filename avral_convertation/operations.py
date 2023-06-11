#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os

from avral import avral
from avral.operation import AvralOperation, OperationException
from avral.io.types import *
from avral.io.responce import AvralResponce


class Converter(AvralOperation):
    def __init__(self):
        super(Converter, self).__init__(
            name="converter",
            inputs=[
                ("input_file", FileType()),
            ],
            outputs=[
                ("output_file", FileType()),
            ],
        )

    def _do_work(self):
        # Получение пути к файлу Excel из входных параметров
        input_file = self.getInput("input_file")

        # Проверка существования файла
        if not os.path.isfile(input_file):
            raise OperationException("Input file does not exist")

        # Формирование команды для вызова скрипта converter.py
        export_file = "result.gpkg"
        cmd = "python " + os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "converter.py"
        )
        cmd = cmd + " --input {input_file} --output {output_file}"
        cmd = cmd.format(
            input_file=input_file,
            output_file=export_file,
        )

        # Выполнение команды
        os.system(cmd)

        # Установка выходного файла
        self.setOutput("output_file", export_file)

        return ()
