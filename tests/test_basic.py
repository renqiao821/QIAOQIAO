import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import qiaoqiao  # noqa: E402


class VersionTest(unittest.TestCase):
    def test_version(self) -> None:
        self.assertEqual(qiaoqiao.__version__, "0.1.0")


if __name__ == "__main__":
    unittest.main()
