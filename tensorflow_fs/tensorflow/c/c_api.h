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

#ifndef TENSORFLOW_C_C_API_H_
#define TENSORFLOW_C_C_API_H_

#include <stddef.h>
#include <stdint.h>

// --------------------------------------------------------------------------
// C API for TensorFlow.
//
// The API leans towards simplicity and uniformity instead of convenience
// since most usage will be by language specific wrappers.
//
// Conventions:
// * We use the prefix TF_ for everything in the API.
// * Objects are always passed around as pointers to opaque structs
//   and these structs are allocated/deallocated via the API.
// * TF_Status holds error information.  It is an object type
//   and therefore is passed around as a pointer to an opaque
//   struct as mentioned above.
// * Every call that has a TF_Status* argument clears it on success
//   and fills it with error info on failure.
// * unsigned char is used for booleans (instead of the 'bool' type).
//   In C++ bool is a keyword while in C99 bool is a macro defined
//   in stdbool.h. It is possible for the two to be inconsistent.
//   For example, neither the C99 nor the C++11 standard force a byte
//   size on the bool type, so the macro defined in stdbool.h could
//   be inconsistent with the bool keyword in C++. Thus, the use
//   of stdbool.h is avoided and unsigned char is used instead.
// * size_t is used to represent byte sizes of objects that are
//   materialized in the address space of the calling process.
// * int is used as an index into arrays.
//
// Questions left to address:
// * Might at some point need a way for callers to provide their own Env.
// * Maybe add TF_TensorShape that encapsulates dimension info.
//
// Design decisions made:
// * Backing store for tensor memory has an associated deallocation
//   function.  This deallocation function will point to client code
//   for tensors populated by the client.  So the client can do things
//   like shadowing a numpy array.
// * We do not provide TF_OK since it is not strictly necessary and we
//   are not optimizing for convenience.
// * We make assumption that one session has one graph.  This should be
//   fine since we have the ability to run sub-graphs.
// * We could allow NULL for some arguments (e.g., NULL options arg).
//   However since convenience is not a primary goal, we don't do this.
// * Devices are not in this API.  Instead, they are created/used internally
//   and the API just provides high level controls over the number of
//   devices of each type.

#ifdef __cplusplus
extern "C" {
#endif

// --------------------------------------------------------------------------
// TF_Version returns a string describing version information of the
// TensorFlow library. TensorFlow using semantic versioning.
extern const char* TF_Version();

// --------------------------------------------------------------------------
// TF_DataType holds the type for a scalar value.  E.g., one slot in a tensor.
// The enum values here are identical to corresponding values in types.proto.
typedef enum {
  TF_FLOAT = 1,
  TF_DOUBLE = 2,
  TF_INT32 = 3,  // Int32 tensors are always in 'host' memory.
  TF_UINT8 = 4,
  TF_INT16 = 5,
  TF_INT8 = 6,
  TF_STRING = 7,
  TF_COMPLEX64 = 8,  // Single-precision complex
  TF_COMPLEX = 8,    // Old identifier kept for API backwards compatibility
  TF_INT64 = 9,
  TF_BOOL = 10,
  TF_QINT8 = 11,     // Quantized int8
  TF_QUINT8 = 12,    // Quantized uint8
  TF_QINT32 = 13,    // Quantized int32
  TF_BFLOAT16 = 14,  // Float32 truncated to 16 bits.  Only for cast ops.
  TF_QINT16 = 15,    // Quantized int16
  TF_QUINT16 = 16,   // Quantized uint16
  TF_UINT16 = 17,
  TF_COMPLEX128 = 18,  // Double-precision complex
  TF_HALF = 19,
  TF_RESOURCE = 20,
} TF_DataType;

// TF_DataTypeSize returns the sizeof() for the underlying type corresponding
// to the given TF_DataType enum value. Returns 0 for variable length types
// (eg. TF_STRING) or on failure.
//extern size_t TF_DataTypeSize(TF_DataType dt);

// --------------------------------------------------------------------------
// TF_Code holds an error code.  The enum values here are identical to
// corresponding values in error_codes.proto.
typedef enum {
  TF_OK = 0,
  TF_CANCELLED = 1,
  TF_UNKNOWN = 2,
  TF_INVALID_ARGUMENT = 3,
  TF_DEADLINE_EXCEEDED = 4,
  TF_NOT_FOUND = 5,
  TF_ALREADY_EXISTS = 6,
  TF_PERMISSION_DENIED = 7,
  TF_UNAUTHENTICATED = 16,
  TF_RESOURCE_EXHAUSTED = 8,
  TF_FAILED_PRECONDITION = 9,
  TF_ABORTED = 10,
  TF_OUT_OF_RANGE = 11,
  TF_UNIMPLEMENTED = 12,
  TF_INTERNAL = 13,
  TF_UNAVAILABLE = 14,
  TF_DATA_LOSS = 15,
} TF_Code;

// --------------------------------------------------------------------------
// TF_Status holds error information.  It either has an OK code, or
// else an error code with an associated error message.
typedef struct TF_Status TF_Status;

// Return a new status object.
extern TF_Status* TF_NewStatus();

// Delete a previously created status object.
extern void TF_DeleteStatus(TF_Status*);

// Record <code, msg> in *s.  Any previous information is lost.
// A common use is to clear a status: TF_SetStatus(s, TF_OK, "");
extern void TF_SetStatus(TF_Status* s, TF_Code code, const char* msg);

// Return the code record in *s.
extern TF_Code TF_GetCode(const TF_Status* s);

// Return a pointer to the (null-terminated) error message in *s.  The
// return value points to memory that is only usable until the next
// mutation to *s.  Always returns an empty string if TF_GetCode(s) is
// TF_OK.
extern const char* TF_Message(const TF_Status* s);
}
#endif