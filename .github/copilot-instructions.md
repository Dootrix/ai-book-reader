# Copilot Instructions for AI Book Reader

## Project Overview
This is an AI-assisted book reader application designed to enhance the reading experience through artificial intelligence features.

## Development Guidelines

### Code Style and Standards
- Write clean, readable, and well-documented code
- Use meaningful variable and function names
- Follow consistent formatting and indentation
- Add comments for complex logic or algorithms

### Project Context
- This is an AI-powered book reading application
- Focus on user experience and accessibility
- Consider performance implications for file processing and AI operations
- Maintain compatibility across different file formats and devices

### Architecture Principles
- Keep components modular and reusable
- Separate concerns between UI, business logic, and AI processing
- Use appropriate design patterns for scalability
- Implement proper error handling and logging

### AI Integration Best Practices
- Handle AI API calls gracefully with proper error handling
- Implement fallback mechanisms when AI services are unavailable
- Consider rate limiting and cost optimization for AI operations
- Support user-provided OpenAI API keys (BYOK - Bring Your Own Key) for enhanced privacy and cost control
- Ensure user privacy and data security when processing book content
- Validate and secure API key storage using environment variables or secure configuration

### Testing Guidelines
- Write unit tests for core functionality
- Test AI integration components thoroughly
- Include edge cases and error scenarios
- Maintain good test coverage for critical paths

### Documentation Standards
- Update README.md with setup and usage instructions
- Document API endpoints and data models
- Include examples for complex features
- Keep documentation current with code changes

### Security Considerations
- Sanitize user inputs, especially file uploads
- Implement proper authentication and authorization if needed
- Secure API keys and sensitive configuration using environment variables or encrypted storage
- Never log or expose user-provided API keys in plain text
- Provide clear warnings about API key security when users input their own keys
- Follow security best practices for file handling

## Specific Guidance for This Repository

### File Processing
- Support multiple book formats (PDF, EPUB, TXT, DOCX, etc.)
- Implement efficient text extraction and processing
- Handle large files gracefully with streaming or chunking

### AI Features
- Implement smart bookmarking and note-taking
- Provide reading comprehension assistance
- Support text summarization and key insights
- Enable semantic search within books
- Allow users to configure their own OpenAI API keys for personalized AI services
- Provide clear UI for API key management with proper security warnings

### User Interface
- Design for readability and eye comfort
- Support different themes (light/dark mode)
- Implement responsive design for various screen sizes
- Ensure accessibility compliance (WCAG guidelines)

### Performance
- Optimize for fast loading and smooth scrolling
- Implement efficient caching strategies
- Minimize memory usage for large documents
- Use lazy loading for content-heavy pages

When contributing to this project, always consider the end-user experience and how features will enhance the reading journey while maintaining performance and security standards.