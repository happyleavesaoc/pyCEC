from typing import List


class CecCommand:
    def __init__(self, cmd=None, dst: int = None, src: int = None,
                 att: List[int] = None, raw: str = None):

        self._src = src
        self._dst = dst
        self._cmd = cmd
        self._att = att
        self._raw = raw

        if raw is not None:
            self.raw = raw
        elif isinstance(cmd, (str,)):
            self.raw = cmd
        else:
            self.src = src
            self.dst = dst
            self.cmd = cmd
            self.att = att

    @property
    def src(self) -> int:
        return self._src

    @src.setter
    def src(self, value: int):
        self._src = value

    @property
    def dst(self) -> int:
        return self._dst

    @dst.setter
    def dst(self, value: int):
        self._dst = value

    @property
    def cmd(self) -> int:
        return self._cmd

    @cmd.setter
    def cmd(self, value: int):
        self._cmd = value

    @property
    def att(self) -> List[int]:
        return self._att if self._att else []

    @att.setter
    def att(self, value: List[int]):
        self._att = value

    @property
    def raw(self) -> str:
        atts = "".join(((":%02x" % i) for i in self.att))
        return "%1x%1x:%02x%s" % (
            self.src if self.src is not None else 0xf, self.dst if self.dst is not None else 0xf, self.cmd, atts)

    @raw.setter
    def raw(self, value: str):
        atts = value.split(':')
        self.src = int(atts[0][0], 16)
        self.dst = int(atts[0][1], 16)
        self.cmd = int(atts[1], 16)
        self.att = list(int(x, 16) for x in atts[2:])

    def __str__(self):
        return self.raw