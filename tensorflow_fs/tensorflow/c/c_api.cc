/* Copyright 2015 The TensorFlow Authors. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
==============================================================================*/

#include "tensorflow/c/c_api.h"

#include <algorithm>
#include <limits>
#include <memory>
#include <vector>

#include "tensorflow/core/lib/core/errors.h"
#include "tensorflow/core/lib/core/status.h"
#include "tensorflow/core/lib/core/stringpiece.h"
#include "tensorflow/core/platform/types.h"
#include "tensorflow/c/version.h"

// The implementation below is at the top level instead of the
// brain namespace because we are defining 'extern "C"' functions.
using tensorflow::error::Code;
using tensorflow::Status;

extern "C" {

// --------------------------------------------------------------------------
const char* TF_Version() { return TF_VERSION_STRING; }

// --------------------------------------------------------------------------
//size_t TF_DataTypeSize(TF_DataType dt) {
  //return static_cast<size_t>(
      //tensorflow::DataTypeSize(static_cast<DataType>(dt)));
//}

// --------------------------------------------------------------------------
struct TF_Status {
  Status status;
};

TF_Status* TF_NewStatus() { return new TF_Status; }

void TF_DeleteStatus(TF_Status* s) { delete s; }

void TF_SetStatus(TF_Status* s, TF_Code code, const char* msg) {
  s->status = Status(static_cast<Code>(code), tensorflow::StringPiece(msg));
}

TF_Code TF_GetCode(const TF_Status* s) {
  return static_cast<TF_Code>(s->status.code());
}

const char* TF_Message(const TF_Status* s) {
  return s->status.error_message().c_str();
}
}

// --------------------------------------------------------------------------