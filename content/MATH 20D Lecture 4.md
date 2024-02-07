---
tags:  
- Type/Note  
- Topic/Differential_Equations  
- Class/MATH_20D  
date:  
- 2024-01-17  
---
  
> [!question] Integrate $\frac{dx}{(9x^2+4)^2}$  
> $\frac{1}{(9x^2+4)^2}=\frac{1}{(9(x^2))}=\frac{1}{81}\frac{1}{\left( x^2+\frac{4}{9} \right)^2}=\frac{1}{81}\frac{1}{\left( \sqrt{ x^2+\left( \frac{2}{3} \right)^2 } \right)^4}$  
> $\to a=\frac{2}{3}\to$ Let $x=\frac{2}{3}\tan \theta$  
> $\implies\frac{1}{(9x^2+4)^2}=\frac{1}{\left( 9\frac{4}{9}\tan^2\theta+4 \right)^2}=\frac{1}{16}\frac{1}{(\tan^2\theta+1)^2}=\frac{1}{16}\frac{1}{\sec^4\theta}$  
> $dx=\frac{2}{3}\sec^2\theta d\theta$  
> $\int \frac{dx}{(9x^2+4)^2}=\int \frac{1}{16}\frac{1}{\sec^4\theta}\frac{2}{3}\sec^2\theta  \, d\theta=\frac{1}{24}\int \frac{d\theta}{\sec^2\theta}$  
> $=\frac{1}{24}\int \cos^2\theta \, d\theta=\frac{1}{48}\int (1+\cos(2\theta)) \, d\theta=\frac{1}{48}\left( \theta+\frac{\sin(2\theta)}{2} \right)+C=\frac{1}{48}(\theta+\sin \theta \cos \theta)+C$  
> $x=\frac{2}{3}\tan \theta\implies \tan \theta=\frac{3x}{2}\implies \theta=\tan^{-1}(\frac{3x}{2})$  
> $\sin \theta \cos \theta=\frac{(opp)(adj)}{(hyp)^2}=\frac{6x}{9x^2+4}$  
> $\frac{1}{48}\tan^{-1}(\frac{3x}{2})+\frac{x}{8(9x^2+4)}+C$  
  
> [!question] Solve the following IVP: $x \frac{dy}{dx}=\frac{x^2+1}{(x+1)^2(y-1)},y(1)=2$  
> 1. Separate: $(y-1)dy=\frac{x^2+1}{x(x+1)^2}dx$  
> 2. Integrate: $\int (y-1) \, dy=\int \frac{x^2+1}{x(x+1)^2} \, dx\implies \frac{y^2}{2}-y=\ln|x|+\frac{2}{x+1}+C$  
> 3. Use initial condition: $x=1,y=2$ to solve for C: $\frac{2^2}{2}-2=\ln|1|+\frac{2}{1+1}+C\implies0=1+C\implies C=-1$  
> Implicit solution: $\frac{y^2}{2}-y=\ln|x|+\frac{2}{x+1}-1$  
> $\frac{y^2}{2}-y=\ln|x|+\frac{2}{x+1}-1$  
> $\implies y^2-2y=2\ln|x|+\frac{4}{x+1}-2$  
> $\implies y^2-2y+1=\ln(x^2)+\frac{4}{x+1}-1$  
> $\implies(y-1)^2=\ln(x^2)+\frac{3-x}{x+1}$  
> $\implies y=1\pm \sqrt{ \ln(x^2)+\frac{3-x}{x+1} }$  
> $2=1\pm \sqrt{ \ln(1)+\frac{3-1}{1+1} }=1\pm \sqrt{ 1 }$ so we take the + version  
> Explicit solution: $y(x)=1+\sqrt{ \ln(x^2)+\frac{3-x}{x+1} }$  
  
> [!note] Homogenous  
> If the RHS of the equation $\frac{dy}{dx}=f(x,y)$ can be expressed as a function of the ratio $\frac{y}{x}$ only, then the equation is said to be **homogenous**. Such equations can always be transformed into separable equations by a change of dependent variable.  
  
> [!question] Solve the equation $\frac{dy}{dx}=\frac{y-4x}{x-y}$  
> $\text{RHS}=\frac{y-4x}{x-y}=\frac{y-4x}{x-y}\frac{\frac{1}{x}}{\frac{1}{x}}=\frac{(y-4x)/x}{(x-y)/x}=\frac{\frac{y}{x}-4}{1-\frac{y}{x}}$  
> $v(x)=\frac{y(x)}{x}\implies y(x)=x\cdot v(x)$  
> Derive with respect to $x$: $\frac{d}{dx}(y(x))=\frac{d}{dx}(x\cdot v(x))\implies \frac{dy}{dx}=v(x)+x\frac{dv}{dx}$  
> $\text{LHS}=\frac{dy}{dx}=v+x\frac{dv}{dx}$  
> $\text{RHS}=\frac{\frac{y}{x}-4}{1-\frac{y}{x}}=\frac{v-4}{1-v}$  
> $v+x\frac{dv}{dx}=\frac{v-4}{1-v}\implies x\frac{dv}{dx}=\frac{v-4}{1-v}-v=\frac{v-4-v+v^2}{1-v}=\frac{v^2-4}{1-v}\implies \frac{dv}{dx}=\left( \frac{1}{x} \right)\left( \frac{v^2-4}{1-v} \right)$  
> 1. Separate $x \text{ and } v$: $\left( \frac{1-v}{v^2-4} \right)dv=\frac{dx}{x}$  
> 2. Integrate $\int \frac{1-v}{v^2-4} \, dv=\int \frac{dx}{x}$  
> $\text{RHS}=\int \frac{dx}{x}=\ln|x|+C$  
> $\text{LHS}=\int \frac{1-v}{v^2-4}dv=\int \left( \frac{-1/4}{v-2} +\frac{-\frac{3}{4}}{v+2}\right) \, dv$ (partial fraction decomp)  
> $=-\frac{1}{4}\ln|v-2|-\frac{3}{4}\ln|v+2|+C$  
> $-\frac{1}{4}\ln|v-2|-\frac{3}{4}\ln|v+2|=\ln|x|+C$  
> $\implies{4}\ln|x|+\ln|v-2|+3\ln|v+2|+4C=0$  
> $\ln|x^4(v-2)(v+2)^3|=C_{1}$  
> $x^4(v-2)(v+2)^3=e^{C_{1}}=C_{2}$  
> $\implies x^2\left( \frac{y}{x}-2 \right)\left( \frac{y}{x}+2 \right)=C_{2}$  
> $x^4(\frac{y-2x}{x})(\frac{y+2x}{x})^3=C_{2}$  
> General solution in implicit form: $\implies(y-2x)(y+2x)^3=C$  
  
> [!definition] Linear First-Order Equation  
> $\frac{dy}{dx}+P(x)y=Q(x)$  
> y: dependent variable, x: independent variable, y(x) unknown  
  
> [!note] Method for solving 1st-Order Linear Equations  
> Example: Find the general solution of $\frac{dy}{dx}-2y=x^2e^x$  
> 1. Convert the given into standard form (if needed). Then compute the **integrating factor** $u(x)$ given by:  
> $u(x)=e^{\int P(x) \, dx}=\text{exp}\left( \int P(x) \, dx \right)$  
> $\int p(x) \, dx=\int (-2) \, dx=-2x$  
> $u(x)=e^{\int p(x) \, dx}=e^{-2x}$  
> So $u(x)=e^{-2x}$ is our integrating factor  
> 2. Multiply $u(x)$ to both sides of the equation in standard form:  
> $u(x) \frac{dy}{dx}+u(x)P(x)y=u(x)Q(x)$  
> $e^{-2x}(y'-2y)=(x^2e^x)e^{-2x}\implies e^{-2x}y'-2e^{-2x}y=x^2e^{-x}$  
> Check if the derivative of $e^{-2x}$ is $-2e^{-2x}$  
> Convert LHS into a single derivative using product rule  
> $(e^{-2x}y)'=x^2e^{-x}$  
> 3. Integrate both sides of $\frac{d}{dx}(u(x)y)=u(x)Q(x)$ then solve for $y$  
> $ye^{-2x}=\int x^2e^{-x} \, dx=-x^2e^{-x}-2xe^{-x}-2e^{-x}+C$  
> $\implies y=e^{2x}(-x^2e^{-x}-2xe^{-x}-2e^{-x}+C)$  
> Explicit form, general solution: $\implies y=-x^2e^x-2xe^x-2e^x+Ce^{2x}$  
> $I=\int x^2e^{-x} \, dx$  
> Let $u=x^2\implies du=2xdx$  
> $dv=e^{-x}dx\implies v=-e^{-x}$  
> So $I=-x^2e^{-x}+\int 2xe^{-x} \, dx=-x^2e^{-x}+2\int xe^-x \, dx$  
> Now we use integration by parts on $\int xe^{-x} \, dx$  
> Let $u=x,dv=e^{-x}dx\implies du=dx,v=-e^{-x}$  
> $\implies \int xe^{-x} \, dx=-xe^{-x}+\int e^{-x} \, dx=-xe^{-x}-e^{-x}+C$  
> $I=-x^2e^{-x}+2(-xe^{-x}-e^{-2}+C)\implies I=-x^2e^{-x}-2xe^{-x}-2e^{-x}+C$  
  
> [!question] Find the general solution of $(1+t^2)\frac{dy}{dt}+4ty=(1+t^2)^{-2}$  
> Convert the given equation into standard form by dividing both sides by $1+t^2$  
> $\to y'+(\frac{4t}{1+t^2})y=\frac{1}{(1+t^2)^3}\implies P(t)=\frac{4t}{1+t^2}$  
> $\int p(t) \, dt=\int \frac{4t}{1+t^2} \, dt=\dots \text{(u-sub }u=1+t^2,du=2tdt)=\int \frac{2du}{u}=2\ln|u|=2\ln(1+t^2)$  
> $u(t)=e^{\int p(t) \, dt}=e^{2\ln(1+t^2)}=e^{\ln((1+t^2)^2)}=(1+t^2)^2$  
> Multiply $u(t)=(1+t^2)^2$ to both sides of the standard form eqn  
> $(1+t^2)^2\left( y'+\left( \frac{4t}{1+t^2} \right)y \right)=\frac{1}{(1+t^2)^3}(1+t^2)^2$  
> $\implies(1+t^2)^2y'+4t(1+t^2)y=\frac{1}{1+t^2}$  
> $\implies y(1+t^2)^2)'=\frac{1}{1+t^2}$  
> $\implies y(1+t^2)^2=\int \frac{1}{1+t^2} \, dt=\arctan(t)+C$  
> $\implies y(t)=\frac{\arctan(t)+C}{(1+t^2)^2}$  
