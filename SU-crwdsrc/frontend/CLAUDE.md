- react-typescript: latest stable version - LSV
- pure html&css, no tailwind or other alternatives
- No redux, use react context and react state
- eslint configuration (4 spaces, semicolons, 2 empty lines after the last import (not the default 1 empty line))
- theme: light and dark
- for each component create a directory (if a component has subcomponents, nest them in the directory as well)
- base url and all descendant URLs should be imported constants, not hardcoded in the source code
- Use `const` over `let`; never `var`
- Strict TypeScript mode enabled
- No `any` type; use proper type definitions
- TypeScript interfaces for all type definitions
- Place `.then()` `.catch()` `.finally()` `.filter()` `.map()` `.forEach()` `.reduce()` `.sort()` `.catch()` on new lines (indented):
- Add blank lines between logical blocks
- Descriptive variable names (no `r`, `v`, `item` for complex objects)
- Extract complex logic into named helper functions
- Leave an empty line at the end of each file
- Format if-else statements, try-catch block like this (single empty line before the else or catch line)
```typescript
try {
  if (x) {
    console.log("ok");

  } else {
    console.log("no");
  }

} catch {
  console.log("error");
}
```