class Solution {
    public String simplifyPath(String path) {
        Stack<String> stack = new Stack<String>();
        Set<String> skip = new HashSet<>(Arrays.asList("..", ".",""));
        for (String c : path.split("/")) {
            if (!stack.empty() && c.equals("..")) {
                stack.pop();
            } else if (!skip.contains(c)) {
                stack.push(c);
            }
        }
        return "/" + String.join("/", stack);
        }
    }
        

