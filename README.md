# SecureWipe

**SecureWipe** is a professional-grade file sanitization utility designed to permanently remove sensitive data from storage media. Unlike standard OS deletion, which only removes file pointers, SecureWipe overwrites the actual data sectors using industry-recognized algorithms, rendering forensic recovery impossible.

## Features

*   **DoD 5220.22-M Compliance**: Implements the US Department of Defense 3-pass overwrite standard.
*   **Gutmann Method**: Offers the Peter Gutmann 35-pass algorithm for maximum security on magnetic media.
*   **Recursive Folder Wiping**: Securely destroys entire directories and their contents.
*   **Anti-Forensics**: Automatically renames files to random alphanumeric strings before deletion to obscure file names in the Master File Table (MFT).
*   **Zero-Trace**: Leaves no temporary files or logs behind.

## Installation

1.  Ensure Python 3.x is installed.
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  Run the application:
    ```bash
    python main.py
    ```
2.  Select the target **File** or **Folder** using the respective buttons.
3.  Choose the desired sanitization algorithm from the dropdown menu.
4.  Click **Erase File** to begin the irreversible destruction process.

---

# SecureWipe (RU)

**SecureWipe** — это профессиональная утилита для безвозвратного удаления конфиденциальных данных. В отличие от стандартного удаления файлов средствами ОС, которое стирает лишь ссылки на файлы, SecureWipe перезаписывает физические сектора данных, используя промышленные алгоритмы, что делает восстановление информации невозможным.

## Возможности

*   **Стандарт DoD 5220.22-M**: Реализация 3-проходного стандарта уничтожения данных Министерства обороны США.
*   **Метод Гутмана**: Алгоритм Питера Гутмана (35 проходов) для максимальной надежности.
*   **Рекурсивное удаление папок**: Полное уничтожение содержимого директорий.
*   **Анти-форензика**: Автоматическое переименование файлов в случайные строки перед удалением для скрытия имен в MFT.
*   **Отсутствие следов**: Программа не создает временных файлов и логов.

## Установка

1.  Убедитесь, что установлен Python 3.x.
2.  Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```

## Использование

1.  Запустите приложение:
    ```bash
    python main.py
    ```
2.  Выберите целевой файл или папку, используя кнопки **File** или **Folder**.
3.  Выберите алгоритм стирания в выпадающем списке.
4.  Нажмите **Erase File** для начала процесса уничтожения.
