#!/usr/bin/env python3
#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import re
import sys

from flipperzero_protobuf.flipperCmd.flipperzero_cmd import main

if __name__ == "__main__":
    sys.argv[0] = re.sub(r"(-script\.pyw|\.exe)?$", "", sys.argv[0])
    sys.exit(main())
