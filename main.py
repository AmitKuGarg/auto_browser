from src.ui.gradio_interface import GradioInterface
import argparse


def main():
    parser = argparse.ArgumentParser(description='Web Scraper and Vector Store')
    parser.add_argument('vectorDir', default='vector_store', help='Vector store directory')
    args = parser.parse_args()
    app = GradioInterface(args.vectorDir)
    app.launch()


if __name__ == "__main__":
    main()
