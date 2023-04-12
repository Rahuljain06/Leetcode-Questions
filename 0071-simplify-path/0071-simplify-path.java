class Solution {
    public String simplifyPath(String path) {
        Stack<String> stack = new Stack<String>();
        String[] skip = {"..", ".", ""};
        for (String c : path.split("/")) {
            if (!stack.empty() && c.equals("..")) {
                stack.pop();
            } else if (!Arrays.asList(skip).contains(c)) {
                stack.push(c);
            }
        }
        return "/" + String.join("/", stack);
        }
    }
        

