from app.models.classification.timm.inference import Inference
from app.models.classification.timm.train import train
import yaml


class InferenceClassification:
	"""Inference Classification model """

	def __init__(self,
				 checkpoint_path: str,
				 model_name: str = "mixnet_s",
				 num_classes: int = 2):
		self.model = Inference(
			checkpoint_path,
			model_name=model_name,
			num_classes=num_classes,
			no_test_pool=True,
		)

	def __call__(self, source):
		return self.model.run(source=source, batch_size=8)

	# TODO: train model and save its checkpoint, then replace the init model with the already trained model
	def train(self, dataset, configuration_file):
		"""
			Train model and save its checkpoint

		Args:
			dataset (str): path/to/dataset
			configuration_file (str): path/to/yaml-file

		Returns:
			the best checkpoint path
		"""
		trained_checkpoint_path = train(self.model.model, dataset, configuration_file)

		trained_checkpoint_path = 'model_best.pth.tar'  # NOTE: For debug only, delete this line later

		self.model = Inference(
			trained_checkpoint_path,
			model_name='mixnet_s',
			num_classes=2,
			no_test_pool=True,
		)

		return trained_checkpoint_path
