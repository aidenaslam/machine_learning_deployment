from logistic_regression_model.parameters.project_parameters import project_path
import os

# It is strongly advised that you do not add any handlers other than
# NullHandler to your library’s loggers. This is because the configuration
# of handlers is the prerogative of the application developer who uses your
# library. The application developer knows their target audience and what
# handlers are most appropriate for their application: if you add handlers
# ‘under the hood’, you might well interfere with their ability to carry out
# unit tests and deliver logs which suit their requirements.
# https://docs.python.org/3/howto/logging.html#configuring-logging-for-a-library


with open(os.path.join(project_path, "VERSION")) as version_file:
    __version__ = version_file.read().strip()
