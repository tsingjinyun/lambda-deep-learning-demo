"""
Copyright 2018 Lambda Labs. All Rights Reserved.
Licensed under
==========================================================================

"""
import tensorflow as tf


class APP(object):
  """ A machine leanring application composed of
      an inputter, a modeler and a runner.
  """
  def __init__(self, args, runner):

    tf.reset_default_graph()

    self.args = args
    self.runner = runner

  def run(self):
    self.runner.run()