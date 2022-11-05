import time

class ProgressBar:
  def __init__(self, progress:int=0, max_value:int=100):
    self.progress = progress
    self.max_value = max_value
  
  def set_max(self, max_value:int) -> None:
    self.max_value = max_value

  def set_progress(self, progress:int) -> None:
    self.progress = progress
  
  def print_progress_bar(self) -> None:
    max_progress_count = 50
    progress = self.progress / self.max_value * 100.0
    progress_count = self.progress * max_progress_count // self.max_value
    bar = "\r["
    bar += ">" if progress_count == 0 else ("=" * (progress_count - 1)) + ">"
    bar += "." * (max_progress_count - progress_count)
    bar += "] "
    bar += "{:>3.1f}".format(progress) + "%"
    print(bar, end='')

  def end(self) -> None:
    print()

if __name__ == "__main__":
  max_value = 110
  delta = 10

  pb = ProgressBar(progress=0, max_value=max_value)
  for progress in range(0, max_value + delta, delta):
    pb.set_progress(progress)
    pb.print_progress_bar()
    time.sleep(0.5)
  pb.end()

