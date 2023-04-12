class Solution {
    public String simplifyPath(String path) {
        Stack<String> stack = new Stack<String>();
        for (String c : path.split("/")) {
            if (!stack.empty() && c.equals("..")) {
                stack.pop();
            } else if (!c.equals("..") && !c.equals(".") && !c.equals("")) {
                stack.push(c);
            }
        }
        return "/" + String.join("/", stack);
        }
    }
        

