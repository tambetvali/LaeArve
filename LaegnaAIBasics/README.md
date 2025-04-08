# AI theory with some of my Laegna mathematical ideas

This is not hard to provide the basics of an AI in simpler manner, where I don't like that the complexity of texts I used myself, and videos, made many conceptions longer and more complex by involving hard math and complicated ideas.

I mix my own text by generations of an AI to continue each topic with the words I use here, giving it also the text from beginning to end.

## AI Components and process

AI is made typically more or less in such way:
1. Deep Learning platforms, such as Torch and TensorFlow, are installed, and some computing components like tensor and cuda cores, more cores of more powerful processing, could be adapted.
2. A _brain_ or a _model_ is made: consisting of brain areas, some (digital) neural networks connected in layers.
  - This _model_ defines input, output types and a sequence of layers, which map it to different levels of precision; for complex architectures, custom-made component structures are applied, or ones introduced in scientific publishments.
  - SmolLM has small models to test models, also Qwen and Llama have 0.5 and 1B models (small ones) as well as bigger models, where 3B is still quite fast. With model size in parameters, it needs at least exponential amounts of resources: matrixes rather scale in square relation when compared to vectors, so for amount of data, there are square amounts of processing involved; the exact nature of this proportion depends on the model: for trivial implementations, to get O factor, you multiply the size of input and output, and get a square of their average: this one I call _exponential function_.
3. A _knowledge_ or a _training_ is made, done: this is fine-tuning process, where the brain is introduced some information or data; training of a _model_ is done by fine-tuning process with a _dataset_, either in form of Q&A (Questions and Answers) or Instruction, Question, Answer, or Question, Answer, Document / Context - I call the later Q&A&D as it's what I need. Q&A form is very general also where Question is the input, where Answer is the output: you train all kinds of DL models and machine learning components to _fit_ a specific data, which would mean it becomes fit, or that it fits them: it finds the scientific model to fit the measurement, essentially, if one could call weight matrix a scientific model.
  - This _knowledge_ is kept inside _weight matrix_.
  - __LitGPT__ is a library you can use for fine-tuning: it's custom, rather simplistic instance you would call open source given that you want simple code. [miniGPT](https://github.com/karpathy/minGPT) is considered a minimal model, but it uses __PyTorch__; I suggest __PyTorch__ but it's a heavy library and thus, given average effort, it's not open source into the bones.
4. The trained model is converted into chatbot, character descriptions, greeting messages, Q&A knowledge as working example could give the _brain_ also some _identity_, to _represent a specific role_.
  - This, for example is GGUF for GPT4All, LM Studio and Jan clients for an AI chatbot.
5. If the trained model, with chatbot, such as model with GPT4All, allow this, documentation can be mapped into embeddings and connected to it. Embeddings use an _AI brain_, a model which can put those documents into multidimensional space of coordinates, so that the model would be able to convert it's input into same multidimension, and/or include it's relevant data such as topic or chat history, and get the closest documents from this, where typically a simpler brain would have the document map: model for mapping, such as _Nomic Embed Text v. 1.5_ I have, is not being fine-tuned, but it only calculates the coordinates in it's pre-trained coordinate space (I call the pre-trained information knowledge). This is called RAG memory.
  - You need to create document folders and add those as Collections, which you can turn on and off in real time.
  - The model would consume the documents easily, if it's pre-trained on similar content, for example being able to generalize and get hints from titles.
  - If the other is _knowledge_, call this and _information_: the model is not definitely creative about this, where the fine-tuning rather creates holistic map of the model, where everything could be concluded into a single matrix.
6. You can use the documentation and experience from chatting, or knowledge about where it could lack information, to train (fine-tune) it further. Sometimes, the initial process for knowledge is called "training" or "initial training", where the refining process is "fine-tuning".

_I asked AI_: how is step of exponential function related to square, where what follows would be level four, then sixteen etc.? Write an answer in one paragraph.

_AI answered_: The step of an exponential function relates to squaring in that it compounds values progressively by multiplying the base repeatedly, leading to rapid growth. For instance, when you square a number (e.g., \( 2^2 = 4 \)), you’re effectively exponentiating it to the second power. Following this logic iteratively as an exponential sequence, the next step, such as raising \( 2 \) to the fourth power (\( 2^{(2^2)} = 2^4 = 16 \)), demonstrates an accelerated growth curve, where each subsequent level is a further exponentiation of the result. This compounding relationship causes exponential functions to outpace polynomial growth significantly as the steps increase, showcasing their mathematical intensity. It's as though squaring is the foundational step, and exponential operations iterate and amplify it with each level.

## DL (deep learning) AI (artificial intelligence) inside: how it works

### Data Structures

#### Tensors

Tensors:
- Tensor is physically very similar to vector (multidimensional coordinate) of it's dimension, or list of it's component length.
- Conception of Tensors is associated with physics and other material sciences or sciences about systems with tensions: for example, fields shape the spatial structure, creating tensions inside it, and producing reactions of the matter inside.
- Typically, the tensor size is static. The input and output layers are iterating over possible inputs and outputs in training and fine-tuning, whereas they calculate outputs for inputs and introduce random factor when being in inference, in actual use. In hidden layers, tensors are then going through different shapes and structures _to get rid of tension_.

So a Tensor could be: [1, 2, 3]; where it's point perhaps with X=1, Y=2 and Z=3 in 3-dimensional coordinate space; it could resemble number, when one dimensional, or point coordinates, when having two dimensions. Hypergeometry appears in fourth dimension, and in any number of dimensions, one could do all the calculations.

So as you would expect from a Tensor: when teaching it, you make it "hot" or melt it, so that it has variable shape (numbers within); when you finish, it would cool down and serve you on cristalline basis until more fine-tuning where it's how again. For fine-tunig a _brain_, or model, to load it with _knowledge_ or data / datasets, you need the _brain_ and _knowledge_: the _model_ and it's _weight matrix_.

**AI addition:**  
Tensors are fundamental data structures in deep learning because they enable efficient representation and manipulation of complex multidimensional data. Unlike simpler structures like scalars (single values) or vectors (one-dimensional arrays), tensors can represent data in multiple dimensions simultaneously—such as a batch of images, where each image is stored as a 3D tensor with width, height, and channel dimensions. This ability to represent and operate on high-dimensional data makes tensors indispensable for modern artificial intelligence models. Additionally, tensors integrate smoothly with parallel computing frameworks (such as CUDA for GPUs), enabling large-scale computations to be executed efficiently during training and inference. While the physical analogy of tensors cooling down and crystallizing is insightful, in practice, their dynamic nature within hidden layers—adjusting shapes and values through operations like matrix multiplication and activation functions—makes them the cornerstone of a model's ability to learn and generalize.

Furthermore, tensors aren't just containers for data; they embody transformations. During training, tensors flow through layers of neural networks, interacting with the model's weight matrices and biases to generate meaningful outputs. Each layer applies mathematical operations to these tensors, gradually refining raw input data into representations that the model can interpret, such as identifying patterns or making predictions. This dynamic interplay between static tensor shapes and the dynamic processing within hidden layers highlights the adaptability of deep learning systems, making tensors not just tools for computation but also integral to the model's conceptual framework.

#### Matrices

Matrices have these properties:
- Matrix is a map of coordinates in two-dimensional space, in regards to dimensionality of it's input and output.
- It's a map of function, with input in columns, output in rows of a matrix.

We use the Matrix _in purpose of multiplication_, and it's associated with position (_weights_ and _biases_ - matrix projection with affine translation like zoom, rotate etc, in _weights_ and the additive operations, such as _pan_ or _move_, in bias; then, the _weights_ zoom and rotate the multidimensional space, while the _biases_ would scroll the resulting view, keeping the projection).

To associate, for example, 3D matrices with 1D for addition, with something you can easily imagine, you need to understand, how 3D is projected and positioned typically in virtual worlds.
- The _coordinate matrix_ is used to _position the objects_: you can map, into this matrix, _affine translations_, which are defined to modern geometry based on the matrices. Objects move and rotate based on this matrix. 3*3 space is used for multiplication and division (which form the affine translation), where one column and one row, both with 3 dimensions as well, are added for addition and multiplication (which forms the movement): the general matrix, which has these operators and operations in ideal space, is created by a theory of one mathematician (well you can find backgrounds yourself with internet and AI, so I am into the theory).
  - _AI_: The matrix used to position objects is called the __Model Matrix__ or __World Matrix__. It defines the transformation applied to the object, such as scaling, rotation, or translation, to position it within the scene.
- The _coordinate space matrix_ is used to _create a perspective or viewport_: This uses the same properties: if the space around you would be an object, you could rotate, resize and move it. It's visible as rotating the space, zooming in and out, and moving the camera.
  - _AI_: The matrix used to create a perspective or viewport is called the __Projection Matrix__. This matrix defines how 3D objects are mapped onto a 2D view, creating the illusion of depth and perspective.

Using Javascript library three.js, you can create those matrices with WebGL:
```javascript
// Initialize Scene, Camera, Renderer
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

// 1. Create a simple object (a Tetrahedron for aesthetics)
const geometry = new THREE.TetrahedronGeometry();
const material = new THREE.MeshBasicMaterial({ color: 0xff6347, wireframe: true });
const tetrahedron = new THREE.Mesh(geometry, material);
scene.add(tetrahedron);

// 2. Position the object using Model Matrix logic
tetrahedron.position.set(0, 0, -5); // Move it away from the camera along Z-axis

// 3. Apply a Perspective Matrix for realistic viewing
camera.position.z = 5; // Leonardo da Vinci-like depth happens here via the camera perspective

// Render the scene
function animate() {
  requestAnimationFrame(animate);
  tetrahedron.rotation.x += 0.01; // Rotate for aesthetics
  tetrahedron.rotation.y += 0.01;
  renderer.render(scene, camera);
}
animate();
```

..continued in few days..