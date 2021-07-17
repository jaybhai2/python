# python

decorator design pattern 


```
# component interface
class component()
	def transform()
		pass

# concrete component		
class SourceData(component)
	def __init__(self, source_data)
		self.source_data = source_data
		
	def transform()
		return self.source_object
		
		
# decorator interface	
class TransformDecorator()
	def transform()
		return self.source_object

# concrete decorator 		
class UpperCaser(TransformDecorator)
	def __init__(self, source_data_object)
		self.SourceDataObject = source_data_object

	def transform()
		new = self.SourceDataObject.transform().upper()
		return new
		
# concrete decorator 		
class SplitToList(TransformDecorator)
	def __init__(self, source_data_object)
		self.SourceDataObject = source_data_object

	def transform()
		new = self.SourceDataObject.transform().split(',')
		return new
		

source = SourceComponent('letter')
new_data = ToList(UpperCaser(source))

new_data.transform()



class FascadaImplement
	
	self.sourcedata = SourceComponent(input)
		
	def to_upper()
		x = UpperCaser(source)
		self.source_data = x.transform
		

		```
		
		
# method cascading
# dataframe.change_column_name().all_upper()

	```
class PlatformDataFrame()
	def __init__(self, data_frame)
		self.data_frame = data_frame
		
	def change_column_name():
		col_renamed = self.data_frame.withColumnRenamed("length", "lenth__m")
		self.data_frame = col_renamed
		return self
		
	def all_upper()
		uppered = some function
		self.data_frame = uppered
		return self
	```

instead of returning self, one can return a new instance return PlatformDataFrame(col_renamed_df), or return a different class that have different method: return CharacteristicJsonClass(cleaned_df) 

like dataframe.read return DataFrameReader class


