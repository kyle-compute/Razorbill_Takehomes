# Razorbill - Programming Requirements

## Core Requirements, what you're expected to know at least faintly.

### Git 
- **Standard Git commands** `stash`, `commit`, `oneline`
- **Branch Management**: `branch`, `checkout`, `merge`, `rebase`
- **Remote Operations**: `clone`, `pull`, `push`, `remote`
- **History & Inspection**: `log`, `diff`, `show`, `blame`
- **Undo & Recovery**: `reset`, `revert`, `reflog`
- **Collaboration**: `fetch`, `merge conflicts`, `pull requests` 

### Python Fundamentals
- **Dataclasses**: `@dataclass` with field metadata and type hints
- **Classes**: Inheritance, special methods (`__init__`, `__str__`, `__repr__`)
- **Type Hints**: List[str], Dict[str, Any], Optional types
- **Context Managers**: `with` statements for file handling

### File Processing
- **CSV Parsing**: `csv.DictReader`, file encoding handling (`utf-8-sig`)
- **PDF Processing**: `pdfplumber` for text extraction, page-by-page processing
- **File I/O**: Path handling with `pathlib`, error handling for missing files

### Data Processing
- **String Manipulation**: Strip, split, dictionary comprehension
- **List Comprehensions**: Data transformation and filtering
- **Dictionary Operations**: `.get()`, key stripping, value cleaning

### Database Skills
**SQLAlchemy:**
- **Models**: Declarative base, Column definitions, table relationships
- **Data Types**: UUID, String, Text, Integer, TIMESTAMP, JSONB, ARRAY
- **Indexes**: Composite indexes, unique constraints
- **Relationships**: `relationship()`, foreign keys, cascade operations
- **Advanced Types**: Vector columns (pgvector), PostgreSQL-specific types

**Database Operations:**
- **CRUD Operations**: Create, read, update, delete patterns
- **Querying**: Filtering, ordering, joins
- **Migrations**: Alembic for schema changes
- **Alembic**: Migration scripts, revision management, downgrade capabilities

### API Development
**FastAPI:**
- **Route Handlers**: `@router.post()`, `@router.get()`
- **Dependencies**: `Depends()` for database sessions, auth
- **Request Handling**: `UploadFile`, form data, JSON bodies
- **Response Models**: Pydantic models for validation
- **Error Handling**: HTTP exceptions, validation errors

**Pydantic:**
- **Models**: Data validation, serialization
- **Field Validation**: Custom validators, required fields
- **Type Coercion**: Automatic type conversion

### Security & HIPAA
**Encryption:**
- **File Encryption**: AES-256 for data at rest
- **Transit Security**: TLS 1.3, HTTPS
- **Field-level Encryption**: Encrypting PHI/PII fields
- **Key Management**: Secure key storage

**Input Validation:**
- **Sanitization**: Input stripping, validation
- **File Type Validation**: MIME type checking
- **SQL Injection Prevention**: Parameterized queries
- **XSS Prevention**: Output encoding

**Authentication:**
- **JWT Tokens**: Token generation, validation
- **Password Hashing**: bcrypt for secure storage
- **Session Management**: Secure cookies, timeout

### Testing
**Python Testing:**
- **Pytest**: Unit tests, fixtures, parametrized tests
- **Mock Objects**: Patching external dependencies
- **Integration Tests**: API endpoint testing
- **Database Tests**: Test database setup/teardown

### DevOps & Infrastructure
**Docker:**
- **Containerization**: Multi-stage builds
- **Docker Compose**: Service orchestration
- **Environment Variables**: Configuration management

**Database Management:**
- **PostgreSQL**: Advanced features, extensions (pgvector)
- **Connection Pooling**: Database connection management
- **Backup/Recovery**: Data protection strategies

## Nice To Have (Secondary Skills)

### Frontend Development
**React/Next.js:**
- **Components**: Functional components with hooks
- **Hooks**: `useState`, `useEffect`, custom hooks
- **Form Handling**: `react-hook-form`, validation schemas
- **TypeScript**: Interfaces, type safety, generics
- **File Upload**: Drag-and-drop, progress tracking

**Frontend Libraries:**
- **UI Components**: Radix UI primitives
- **Styling**: Tailwind CSS classes
- **State Management**: Context API, prop drilling

**Frontend Testing:**
- **Jest**: Component testing, snapshot testing
- **React Testing Library**: User interaction testing

### AI/ML Integration
**Transformers & Embeddings:**
- **HuggingFace**: `AutoTokenizer`, `AutoModel`
- **PyTorch**: Tensor operations, device management (CPU/GPU)
- **Embeddings**: Vector generation, normalization, mean pooling
- **Batch Processing**: Efficient processing of multiple texts

**Vector Operations:**
- **NumPy**: Array operations, vector mathematics
- **Similarity Search**: Cosine similarity, vector indexing
- **Dimensionality**: 768-dimensional vectors (BioBERT)

### Search & Information Retrieval
**Search Implementation:**
- **Multi-tier Search**: Keyword → Vector → BM25 fallback
- **Vector Search**: Cosine similarity, embedding comparison
- **Text Search**: ILIKE operations, full-text search
- **Result Merging**: Weighted scoring, deduplication

**Text Processing:**
- **Chunking**: Document segmentation, overlapping windows
- **Metadata Extraction**: Keywords, categories, medical codes
- **Categorization**: LLM-powered classification

### External APIs
**LLM Integration:**
- **Groq API**: Chat completions, streaming responses
- **Prompt Engineering**: System prompts, few-shot examples
- **Token Management**: Counting, cost optimization
- **Error Handling**: API failures, rate limiting

### Performance & Optimization
**Database Performance:**
- **Indexing Strategy**: Query optimization
- **Query Analysis**: EXPLAIN plans, bottleneck identification
- **Connection Management**: Pool sizing, timeout handling

**Async Operations:**
- **Async/Await**: Concurrent file processing
- **Background Tasks**: Celery or similar for long jobs
- **Batch Processing**: Efficient bulk operations

### Monitoring & Logging
**Application Monitoring:**
- **Structured Logging**: JSON format, correlation IDs
- **Error Tracking**: Sentry integration
- **Performance Metrics**: Response times, throughput
- **Health Checks**: Service status monitoring

---

**Must be proficient in all "Must Be Able To" sections. "Nice To Have" skills are beneficial but not required for the role.**