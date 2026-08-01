from src.pipeline.data_pipeline import DataPipeline



pipeline = DataPipeline()
df = pipeline.run()

print(df.shape)
print(df.head())