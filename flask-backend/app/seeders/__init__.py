from flask.cli import AppGroup


seed_cmd = AppGroup("seed")

@seed_cmd.command("all")
def seed_all():
  pass

@seed_cmd.command("undo")
def seed_undo():
  pass
