# Python Exceptions for AWS AI Services

## Amazon SageMaker

1. **`sagemaker.exceptions.SageMakerError`**
   - Base exception for all errors related to SageMaker operations.

2. **`sagemaker.exceptions.TrainingJobFailure`**
   - Raised when a training job fails.

3. **`sagemaker.exceptions.EndpointNotFound`**
   - Raised when the specified endpoint is not found.

4. **`sagemaker.exceptions.ModelNotFound`**
   - Raised when the specified model is not found.

5. **`sagemaker.exceptions.InvalidInputData`**
   - Raised for invalid input data during training or inference.

6. **`sagemaker.exceptions.ResourceNotFound`**
   - Raised when a requested resource (e.g., training job, endpoint) does not exist.

## Amazon Bedrock

1. **`botocore.exceptions.BotoCoreError`**
   - Base exception for all errors related to AWS SDK (Boto3) operations, including those for Bedrock.

2. **`botocore.exceptions.ClientError`**
   - Raised for general client-side errors in AWS services, including Bedrock.

3. **`botocore.exceptions.ParamValidationError`**
   - Raised when parameters provided to a Bedrock API call are invalid or missing.

4. **`botocore.exceptions.S3UploadFailedError`**
   - Raised when an upload to an S3 bucket fails, which could affect Bedrock operations if data storage is involved.

## General AWS SDK (Boto3) Exceptions

1. **`boto3.exceptions.Boto3Error`**
   - Base exception for all Boto3-related errors.

2. **`boto3.exceptions.NoCredentialsError`**
   - Raised when AWS credentials are not found or invalid.

3. **`boto3.exceptions.PartialCredentialsError`**
   - Raised when incomplete AWS credentials are provided.

4. **`boto3.exceptions.S3UploadFailedError`**
   - Raised when an S3 upload fails, potentially affecting AI services relying on S3 storage.
