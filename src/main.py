import os
import shutil
from textnode import *

def copy_static(src, dst):
    # Remove destination directory if it exists
    if os.path.exists(dst):
        shutil.rmtree(dst)
    # Recursively copy all files and directories
    def recursive_copy(s, d):
        if not os.path.exists(d):
            os.mkdir(d)
        for item in os.listdir(s):
            src_path = os.path.join(s, item)
            dst_path = os.path.join(d, item)
            if os.path.isdir(src_path):
                recursive_copy(src_path, dst_path)
            else:
                shutil.copy(src_path, dst_path)
                print(f"Copied: {dst_path}")
    recursive_copy(src, dst)

def main():
    node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(node)
    # Copy static files to public directory
    static_dir = os.path.join(os.path.dirname(__file__), "..", "static")
    public_dir = os.path.join(os.path.dirname(__file__), "..", "public")
    copy_static(static_dir, public_dir)

main()